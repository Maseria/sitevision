from create_cognito import setup_user_pool
from create_dynamodb import create_incident_table
from deploy_lambda import deploy_lambda
from create_apigateway import deploy_api

import time

def deploy_infrastructure():
   # create user pool
   print("Creating user pool")
#    setup_user_pool()

#    time.sleep(10)

#    # create dynamodb table

#    print("creating dynamodb table")
#    create_incident_table()
   
#    time.sleep(10)

#    # deploy our lambda function

#    print("Deploying lambda functions")
   deploy_lambda('CreateIncident', 'insertincident.lambda_handler', 'lambda/insertincident.py')
   deploy_lambda('GetIncidents', 'getincident.lambda_handler', 'lambda/getincident.py')
   deploy_lambda('DeleteIncident', 'deleteincident.lambda_handler', 'lambda/deleteincident.py')

#    time.sleep(20)

#    # deploy our API

#    deploy_api()

if __name__ == "__main__":
    deploy_infrastructure()

