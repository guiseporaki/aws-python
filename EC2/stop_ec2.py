import boto3
from botocore.exceptions import NoCredentialsError, ClientError

def stop_ec2_instance(instance_id):
    try:
        ec2 = boto3.client('ec2')
        ec2.stop_instances(InstanceIds=[instance_id])
        print(f"Instancia {instance_id} detenida con éxito.")
    
    except (NoCredentialsError, ClientError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    stop_ec2_instance('i-0e1734e323b40e59d')  # Reemplaza con tu Instance ID
