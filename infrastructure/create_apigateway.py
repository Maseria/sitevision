import boto3

api = boto3.client('apigateway')
lambda_client = boto3.client('lambda')

# 1. Create REST API
api_resp = api.create_rest_api(name="SiteVisionAPI")
api_id = api_resp['id']

# 2. Get root resource
root_id = api.get_resources(restApiId=api_id)['items'][0]['id']

# 3. Create /incident resource
resource = api.create_resource(
    restApiId=api_id,
    parentId=root_id,
    pathPart='incident'
)
res_id = resource['id']

def add_lambda_route(function_name, method):
    lambda_arn = lambda_client.get_function(FunctionName=function_name)['Configuration']['FunctionArn']
    
    api.put_method(
        restApiId=api_id,
        resourceId=res_id,
        httpMethod=method,
        authorizationType='NONE'
    )
    
    api.put_integration(
        restApiId=api_id,
        resourceId=res_id,
        httpMethod=method,
        type='AWS_PROXY',
        integrationHttpMethod='POST',
        uri=f'arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/{lambda_arn}/invocations'
    )

    lambda_client.add_permission(
        FunctionName=function_name,
        StatementId=f'api-{method}-{function_name}',
        Action='lambda:InvokeFunction',
        Principal='apigateway.amazonaws.com',
        SourceArn=f'arn:aws:execute-api:us-east-1:135808961985:{api_id}/*/{method}/incident'
    )

add_lambda_route('CreateIncident', 'POST')
add_lambda_route('GetIncidents', 'GET')
add_lambda_route('DeleteIncident', 'DELETE')


def deploy_api():
    # Deploy the API
    api.create_deployment(restApiId=api_id, stageName='prod')
    print(f"✅ API URL: https://{api_id}.execute-api.us-east-1.amazonaws.com/prod/incident")

