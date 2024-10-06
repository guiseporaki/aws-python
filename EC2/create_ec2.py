import boto3
from botocore.exceptions import NoCredentialsError, ClientError

def create_ec2_instance():
    try:
        ec2 = boto3.client('ec2')
        response = ec2.run_instances(
            ImageId='ami-0abcdef1234567890',  # Reemplaza con tu AMI ID
            InstanceType='t2.micro',
            KeyName='my-key-pair',  # Reemplaza con tu nombre de clave
            MinCount=1,
            MaxCount=1,
            TagSpecifications=[{
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name', 'Value': 'MyNewEC2Instance'}]
            }]
        )
        print(f"Instancia creada con ID: {response['Instances'][0]['InstanceId']}")
    
    except (NoCredentialsError, ClientError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_ec2_instance()
