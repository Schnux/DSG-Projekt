import json

def logItem(event, context):
    try:
        for r in event.get('Records'):
            if r['eventName'] == 'INSERT':
                print("Handling INSERT event!")
                newImage = r['dynamodb']['NewImage']
                newID = newImage['ID']['S']
                print('New row added to DB with ID = ' + newID)
                print("Done handling INSERT event!")

    except Exception as e:
        print(e)
        return "Ooops!"
