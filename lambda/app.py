import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    if event['httpMethod'] == 'GET':
        item_id = event['queryStringParameters']['id']
        response = table.get_item(Key={'id': item_id})
        return {
            'statusCode': 200,
            'body': json.dumps(response.get('Item', {}))
        }

    elif event['httpMethod'] == 'POST':
        data = json.loads(event['body'])
        table.put_item(Item=data)
        return {
            'statusCode': 201,
            'body': json.dumps({'message': 'Item added'})
        }
