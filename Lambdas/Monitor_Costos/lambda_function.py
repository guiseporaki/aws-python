import json
import boto3
import os
from datetime import datetime, timedelta

# Inicializar los clientes de AWS
ce_client = boto3.client('ce')  # Cost Explorer
sns_client = boto3.client('sns')

def lambda_handler(event, context):
    # Definir el rango de fechas para obtener los costos de AWS
    end_date = datetime.utcnow().date()
    start_date = end_date - timedelta(days=1)
    
    # Formatear las fechas para la consulta
    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')

    # Obtener datos de costos del día anterior
    response = ce_client.get_cost_and_usage(
        TimePeriod={
            'Start': start_date_str,
            'End': end_date_str
        },
        Granularity='DAILY',
        Metrics=['UnblendedCost']
    )
    
    # Extraer el costo total
    cost_items = response['ResultsByTime']
    total_cost = 0
    for item in cost_items:
        amount = item['Total']['UnblendedCost']['Amount']
        total_cost += float(amount)
    
    # Crear el mensaje con el total de costos
    message = f'Total AWS cost for {start_date_str} was ${total_cost:.2f}'

    # Enviar el informe a través de SNS
    sns_topic_arn = os.environ['SNS_TOPIC_ARN']  # Establecer el ARN del SNS en las variables de entorno
    sns_client.publish(
        TopicArn=sns_topic_arn,
        Subject=f'AWS Cost Report for {start_date_str}',
        Message=message
    )

    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }
