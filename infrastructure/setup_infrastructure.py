import create_apigateway,create_cognito,create_dynamodb,deploy_lambda

## create cognito user ID and pool for authorization and authentication

create_cognito.setup_user_pool()

## create  dynamo DB table

create_dynamodb.create_incident_table()

## deploy lambda functions

deploy_lambda.deploy_lambda('CreateIncident', 'insertincident.lambda_handler', 'lambda/insertincident.py')
deploy_lambda.deploy_lambda('GetIncidents', 'getincident.lambda_handler', 'lambda/getincident.py')
deploy_lambda.deploy_lambda('DeleteIncident', 'deleteincident.lambda_handler', 'lambda/deleteincident.py')


## create API gateway

create_apigateway.deploy_api()