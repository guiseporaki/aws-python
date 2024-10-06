import boto3

def listar_buckets_S3():
    # Crear un cliente de S3
    s3 = boto3.client('s3')

    try:
        # Obtener lista de buckets
        respuesta = s3.list_buckets()

        # Extraer el nombre de los buckets
        buckets = [bucket['Name'] for bucket in respuesta['Buckets']]
        
        if buckets:

            print("Buckets en tu cuenta S3:")
            for bucket in buckets:
                print(f"- {bucket}")

        else:
            print("No se encontraron buckets en tu cuenta.")

    except Exception as e:
        print(f"Error al listar buckets: {str(e)}")

# Solo se ejecuta si es el script principal
if __name__ == "__main__":
    listar_buckets_S3()