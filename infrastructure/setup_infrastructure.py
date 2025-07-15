from create_cognito import setup_user_pool
from create_dynamodb import create_incident_table
from deploy_lambda import deploy_lambda
from create_apigateway import deploy_api

def deploy_infrastructure():
   # create user pool
   setup_user_pool()

   # create dynamodb table

   create_incident_table()

   # deploy our lambda function

   deploy_lambda('CreateIncident', 'insertincident.lambda_handler', 'lambda/insertincident.py')
   deploy_lambda('GetIncidents', 'getincident.lambda_handler', 'lambda/getincident.py')
   deploy_lambda('DeleteIncident', 'deleteincident.lambda_handler', 'lambda/deleteincident.py')

   # deploy our API

   deploy_api()

if __name__ == "__main__":
    deploy_infrastructure()

