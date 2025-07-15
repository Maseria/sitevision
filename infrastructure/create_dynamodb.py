import boto3

dynamodb = boto3.client('dynamodb')

def create_incident_table():
    try:
        dynamodb.create_table(
            TableName='Incident',
            KeySchema=[{'AttributeName': 'incidentId', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'incidentId', 'AttributeType': 'S'}],
            BillingMode='PAY_PER_REQUEST'
        )
        print("✅ Incidents table created.")
    except dynamodb.exceptions.ResourceInUseException:
        print("⚠️ Table already exists.")


