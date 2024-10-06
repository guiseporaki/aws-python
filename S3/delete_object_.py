import boto3

def eliminar_archivo():
    s3 = boto3.client('s3')

    # Variables a modificar
    bucket_name = "paraguasnosino"
    nombre_objeto = "archivo.txt"

    try:
        # Eliminar el objeto del bucket
        s3.delete_object(Bucket=bucket_name, Key=nombre_objeto)
        print(f"El objeto '{nombre_objeto}' ha sido eliminado del bucket '{bucket_name}'.")
    except Exception as e:
        print(f"Ocurrió un error al intentar eliminar el objeto: {e}")

if __name__ == '__main__':
    eliminar_archivo()


    