import json
import boto3
import os
def handler(event,context):
#add item to a dynamoDB table using id as primary key fom path /items/{id}
#use table from Environment variable ITEMTBL_TABLE_NAME
#name,price, category are the attributes of the item from querystring
#Return HTTP status code 200 if successful

    dynamodb= boto3.resource('dynamodb')
    table= dynamodb.Table(os.environ['ITEMTBL_TABLE_NAME'])
    id=event['pathParameters']['id']
    name=event['queryStringParameters']['name']
    price=event['queryStringParameters']['price']
    category=event['queryStringParameters']['category']

    table.put_item(
    Item={
    'id':id,
    'name':name,
    'price':price,
    'category':category
    }
    )

    return {
    'statusCode':200,
    'body': json.dumps('Items added to table')
    }

