import json
import boto3

sns_client = boto3.client('sns')

def lambda_handler(event, context):
    # Procesar los hallazgos de Macie
    findings = event['detail']['findings']
    
    for finding in findings:
        # Buscar solo hallazgos de PII
        if 'PII' in finding['category']:
            # Extraer detalles clave del hallazgo
            finding_name = finding['title']
            resource_name = finding['resourcesAffected']['s3Bucket']['name']
            object_name = finding['resourcesAffected']['s3Object']['key']

            # Formatear el mensaje
            message = (f"Amazon Macie detectó PII en un objeto de S3.\n"
                       f"Nombre del bucket: {resource_name}\n"
                       f"Nombre del objeto: {object_name}\n"
                       f"Detalles del hallazgo: {finding_name}")

            # Enviar la notificación por SNS
            sns_client.publish(
                TopicArn='arn:aws:sns:REGION:ACCOUNT_ID:macie-pii-alerts',  # Reemplaza por el ARN de tu topic SNS
                Message=message,
                Subject='¡Alerta de PII detectada por Amazon Macie!'
            )

    return {
        'statusCode': 200,
        'body': json.dumps('Notificación enviada exitosamente')
    }
