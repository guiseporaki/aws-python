import boto3
import csv
import os
from io import StringIO
from datetime import datetime

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = 'bucket-informes-s3'  # Nombre del bucket a analizar
    output_bucket = 'bucket-informes-s3'  # Donde almacenar el informe

    # Obtener la lista de objetos en el bucket
    response = s3.list_objects_v2(Bucket=bucket_name)
    
    if 'Contents' not in response:
        return {
            'statusCode': 200,
            'body': f'El bucket {bucket_name} está vacío o no se encontró.'
        }
    
    objects = response['Contents']
    
    # Calcular el número total de objetos y el tamaño total
    total_objects = len(objects)
    total_size = sum([obj['Size'] for obj in objects])
    
    # Crear el archivo CSV
    csv_output = StringIO()
    csv_writer = csv.writer(csv_output)
    
    # Escribir el encabezado
    csv_writer.writerow(['Nombre del Objeto', 'Última Modificación', 'Tamaño (bytes)'])
    
    # Escribir los detalles de cada objeto
    for obj in objects:
        csv_writer.writerow([obj['Key'], obj['LastModified'], obj['Size']])
    
    # Añadir un resumen al final
    csv_writer.writerow([])
    csv_writer.writerow(['Total de Objetos', total_objects])
    csv_writer.writerow(['Tamaño Total (bytes)', total_size])
    
    # Generar un nombre de archivo único basado en la fecha
    file_name = f'informe-s3-{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.csv'
    
    # Subir el archivo CSV a S3
    s3.put_object(
        Bucket=output_bucket,
        Key=file_name,
        Body=csv_output.getvalue(),
        ContentType='text/csv'
    )
    
    return {
        'statusCode': 200,
        'body': f'Informe generado y guardado en {file_name}'
    }
