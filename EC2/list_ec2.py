import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

def list_ec2_instances():
    try:
        # Crear un cliente EC2 usando boto3
        ec2_client = boto3.client('ec2')
        
        # Describir las instancias
        response = ec2_client.describe_instances()
        
        # Recorrer las reservas e instancias
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                instance_type = instance['InstanceType']
                state = instance['State']['Name']
                launch_time = instance['LaunchTime']
                
                print(f"ID de la instancia: {instance_id}")
                print(f"Tipo de instancia: {instance_type}")
                print(f"Estado: {state}")
                print(f"Hora de lanzamiento: {launch_time}")
                print('-' * 40)
    
    except NoCredentialsError:
        print("Error: No se encontraron credenciales. Asegúrate de que has configurado tus credenciales de AWS correctamente.")
    
    except PartialCredentialsError:
        print("Error: Credenciales incompletas. Verifica tu configuración de credenciales.")
    
    except ClientError as e:
        print(f"Error al comunicarse con AWS: {e}")
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    list_ec2_instances()
