import json
import boto3
from boto3.dynamodb.conditions import Key
from datetime import date

dynamodb = boto3.resource('dynamodb')
client = boto3.client('events')


def updateItem(event, context):
    table = dynamodb.Table('vaccTable')
    try:
        response = table.update_item(
            Key={
                'ID': event["ID"]
            },
            UpdateExpression="SET Name= :n, Vorname= :v, Mail= :m, Geburtstag= :g, PLZ= :plz, Geschlecht= :ge, Priorisierungsgruppe= :p",
            ExpressionAttributeValues={
                ':n': event["name"],
                ':v': event["vorname"],
                ':m': event["mail"],
                ':g': event["geburtstag"],
                ':plz': event["plz"],
                ':ge': event["geschlecht"],
                ':p': event["priorisierungsgruppe"]
            },
            ReturnValues="UPDATED_NEW"
        )
        return response
    except KeyError as e: 
        return "Problem beim Aktualisieren!"


def updatePrio(event, context):
    #todo
    table = dynamodb.Table('vaccTable')
    id = event["ID"]

    birthday = table.query( KeyConditionExpression=Key('ID').eq(id))

    splitDate = birthday["Items"][0]["Geburtstag"].split("-")
    birthDate = date(int(splitDate[2]), int(splitDate[1]), int(splitDate[0]))

    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))

    if age >= 60:
        prio = 1
    elif age < 60 and age >= 40:
        prio = 2
    else:
        prio = 3

    try:
        response = table.update_item(
            Key={
                'ID': id
            },
            UpdateExpression="set Priorisierungsgruppe = :p",
            ExpressionAttributeValues={
                ':p': prio
            },
            ReturnValues="UPDATED_NEW"
        )
        return response
    except KeyError as e:
        return e