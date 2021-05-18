# import requests
import boto3


def query_dynamo():
    dynamodb = boto3.client('dynamodb', region_name="us-east-1")

    response = dynamodb.get_item(
        TableName='todo-table-sam-app',
        Key={
            'cognito-username': {'S': 'fthiagomedeiros'},
            'id': {'S': '10'}
        }
    )

    print(response['Item'])
    return response['Item']