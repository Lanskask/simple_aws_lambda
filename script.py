import json
import boto3
import os
from uuid import uuid4

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.getenv('DYNAMODB_TABLE'))


def lambda_handler(event, context):
    if event['httpMethod'] == 'POST':
        # Add data to DynamoDB table
        item = json.loads(event['body'])
        item['id'] = str(uuid4())
        table.put_item(Item=item)
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Item added', 'item': item})
        }
    elif event['httpMethod'] == 'GET' and event['path'] == '/items':
        # Retrieve all records from DynamoDB table
        response = table.scan()
        return {
            'statusCode': 200,
            'body': json.dumps({'items': response['Items']})
        }
    elif event['httpMethod'] == 'GET' and event['path'] == '/hello':
        # Simple Hello World response
        return {
            'statusCode': 200,
            'body': json.dumps('Hello, World!')
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Unsupported method'})
        }