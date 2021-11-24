import json
import boto3


client = boto3.resource('dynamodb')

def writeItem(event, context):

    # 1 Loading parametrs
    id = event["ID"]
    name = event["Name"]
    vorname = event["Vorname"]
    studiengang = event["Studiengang"]

    # 2 Selecting table
    table = client.Table('studentTable')

    # 3 Creating new Item
    table.put_item(Item= {'ID': id, 'Name': name, 'Vorname': vorname, 'Studiengang': studiengang})

    return 'The given ID ' + id + ' was inserted to the table.'
