import json
import boto3

# Create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# Use the DynamoDB object to select our table
table = dynamodb.Table('Incident')

# Define the handler function that the Lambda service will use as an entry point
def lambda_handler(event, context):
    # Extract values from the event object we got from the Lambda service and store in variables
    
    incidentid = event['incidentid']
    # Write incident data to the DynamoDB table and save the response in a variable
    response = table.delete_item(
        Item={
            'incidentid': incidentid,
        }
    )
    
    # Return a properly formatted JSON object
    return {
        'statusCode': 200,
        'body': json.dumps('Incident data has been deleted successfully!')
    }
