import json
import boto3

client = boto3.client('lambda')

def mainTest(event, context):
    
    # writeItem
    inputParams = {
        "ID" : "1",
        "Name" : "Huseynli",
        "Vorname": "Telman",
        "Studiengang": "Angewandte Informatik"
    } 
    response = client.invoke(
        FunctionName = "arn:aws:lambda:eu-central-1:524748656081:function:dsg-project-1-dev-writeItem",
        InvocationType = 'RequestResponse',
        Payload = json.dumps(inputParams)
    )
    responseOfWrite = json.load(response["Payload"])
    print("Response of writeItem\n")
    print(responseOfWrite)

    print("\n")

    # readItem
    inputParams = {
        "ID" : "1"
    }
    response = client.invoke(
        FunctionName = "arn:aws:lambda:eu-central-1:524748656081:function:dsg-project-1-dev-readItem",
        InvocationType = 'RequestResponse',
        Payload = json.dumps(inputParams)
    )
    responseOfRead = json.load(response["Payload"])
    print("Response of readItem\n")
    print(responseOfRead)
