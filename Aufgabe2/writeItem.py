import json
import boto3
from datetime import date
from datetime import datetime

client = boto3.resource('dynamodb')


def writeItem(event, context):
    table = client.Table('vaccTable')

    # calculating priority
    splitDate = event['geburtstag'].split("-")
    birthDate = date(int(splitDate[2]), int(splitDate[1]), int(splitDate[0]))
    today = date.today()
    current_datetime = datetime.now()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))

    if age >= 60:
        prio = 1
    elif age < 60 and age >= 40:
        prio = 2
    else:
        prio = 3

    # calculating ID
    id = int(str(current_datetime.year) + str(current_datetime.month) + str(current_datetime.day) + str(current_datetime.hour) + str(current_datetime.minute) + str(current_datetime.second) + str(current_datetime.microsecond))

    try:
        # adding entry to the tab
        table.put_item(Item= {   
                            'ID': id,
                            'Name': event["name"], 
                            'Vorname': event["vorname"], 
                            'Mail': event["mail"], 
                            'Geburtstag': event["geburtstag"], 
                            'PLZ': event["plz"], 
                            'Geschlecht': event["geschlecht"],
                            'Priorisierungsgruppe': prio } )

        return "Entry added!"
    except KeyError as e:
        return "Something went wrong ..."