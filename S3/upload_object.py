import boto3

def upload_object():

    s3 = boto3.client('s3')

    # Nombre del bucket y archivo a subir
    bucket_name = 'paraguasnosino'
    local_file = 'C:\\Users\\Tardes\\Desktop\\NotasdeSalida\\python\\scripts\\S3\\ficheroLocal.txt'
    object_name = 'archivo_subido'

    try:
        s3.upload_file(local_file, bucket_name, object_name)
        print(f"Has subido el archivo {local_file} que guardará como objeto en el bucket {bucket_name}, la key del objeto será {object_name}")

    except FileNotFoundError:
        print("El archivo no se encontró. Verifica la ruta.")
    except Exception as e:
        print(f"Ocurrió un error:{e}")


if __name__ == '__main__':
    upload_object()