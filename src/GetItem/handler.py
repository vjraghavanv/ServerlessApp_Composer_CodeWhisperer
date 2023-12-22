import json
import os
def handler(event,context):
#Use table from Environment variable ITEMTBL_TABLE_NAME
#Use if from event path parameter /items/{id}
#Get item from a dynamoDB table using id as primary key
#Return item as JSON object
#Return HTTP status code 200 if item is found
#Return HTTP status code 404 if item is not found
    dynamodb = boto3.resource('dynamodb')
    table = dynamoDB.Table(os.environ['ITEMTBL_TABLE_NAME'])
    id=event['pathParameters']['id']
    item = table.get_item(Key={'id':id})
    if 'Item' in item:
        return {
            'statusCode': 200,
            'body': json.dumps(item['Item'])
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'Item not found'})
        }