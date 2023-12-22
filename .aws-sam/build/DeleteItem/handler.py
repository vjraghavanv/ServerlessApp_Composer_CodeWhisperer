import json
import os
import boto3
def handler(event,context):

#delete item from a dynamoDB table using id as primary key from path /items/{id}
#use table from Environment variable ITEMTBL_TABLE_NAME
#retrun status code 200 if successful
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['ITEMTBL_TABLE_NAME'])
    id=event['pathParameters']['id']
    table.delete_item(
        Key={
            'id':id
        }
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Item deleted successfully')
    }