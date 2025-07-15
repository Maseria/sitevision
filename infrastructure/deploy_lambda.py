import boto3, json, zipfile, os

def zip_lambda(source_file, zip_name):
    with zipfile.ZipFile(zip_name, 'w') as z:
        z.write(source_file, arcname=os.path.basename(source_file))

iam = boto3.client('iam')
lambda_client = boto3.client('lambda')

rolename = input("Enter a role name to deploy lambda: ")

role = iam.create_role(
    RoleName=f'{rolename}',
    AssumeRolePolicyDocument=json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": {"Service": "lambda.amazonaws.com"},
            "Action": "sts:AssumeRole"
        }]
    })
)

iam.attach_role_policy(
    RoleName=f'{rolename}',
    PolicyArn='arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess'
)
iam.attach_role_policy(
    RoleName=f'{rolename}',
    PolicyArn='arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole'
)

# Wait for IAM role to propagate before creating Lambda
import time; time.sleep(10)

def deploy_lambda(name, handler, filename):
    zip_lambda(filename, f'{name}.zip')
    with open(f'{name}.zip', 'rb') as f:
        return lambda_client.create_function(
            FunctionName=name,
            Runtime='python3.9',
            Role=role['Role']['Arn'],
            Handler=handler,
            Code={'ZipFile': f.read()},
            Timeout=15,
            MemorySize=128
        )

