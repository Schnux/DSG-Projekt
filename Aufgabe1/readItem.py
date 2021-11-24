import json
import boto3


client = boto3.resource('dynamodb')

def readItem(event, context):
    #1 Getting parametrs
    id = event["ID"]

    # 2 Selecting table
    table = client.Table('studentTable')

    #3 Looking for item
    result = table.get_item(Key= {'ID': id})
    
    try:
        return result["Item"]
    except KeyError as e:
        return "this " + id +" is not found!"