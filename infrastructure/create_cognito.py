import boto3, json

cognito = boto3.client('cognito-idp')

def setup_user_pool():
    pool = cognito.create_user_pool(PoolName="SiteVisionUserPool")
    pool_id = pool['UserPool']['Id']

    client = cognito.create_user_pool_client(
        UserPoolId=pool_id,
        ClientName="WebAppClient",
        GenerateSecret=False,
        ExplicitAuthFlows=["ALLOW_USER_PASSWORD_AUTH", "ALLOW_REFRESH_TOKEN_AUTH"]
    )
    client_id = client['UserPoolClient']['ClientId']

    print("✅ User Pool ID:", pool_id)
    print("✅ Client ID:", client_id)
    return pool_id, client_id

setup_user_pool()