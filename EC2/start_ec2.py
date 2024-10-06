import boto3
from botocore.exceptions import NoCredentialsError, ClientError

def start_ec2_instance(instance_id):
    try:
        ec2 = boto3.client('ec2')
        ec2.start_instances(InstanceIds=[instance_id])
        print(f"Instancia {instance_id} iniciada con éxito.")
    
    except (NoCredentialsError, ClientError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    start_ec2_instance('i-0e1734e323b40e59d')  # Reemplaza con tu Instance ID
