import boto3

def descargar_archivo():
    s3 = boto3.client('s3')
    
    # Nombre de las variables que tendrás que modificar
    bucket_name = "paraguasnosino"
    nombre_objeto = "archivo_subido"
    archivo_descargado = "fileDownloaded.txt"
    
    try:
        s3.download_file(bucket_name, nombre_objeto, archivo_descargado)
        print(f"Archivo {nombre_objeto} se ha descargado localmente con el nombre {archivo_descargado}")

    except FileNotFoundError:
        print("El archivo no se encontró en el bucket.")
    except Exception as e:
        print(f"Ocurrió un error durante la descarga: {e}")

if __name__ == '__main__':

    descargar_archivo()