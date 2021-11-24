import json
import boto3


client = boto3.client('lambda')

def makeSentence(event, context):
    # Defining variables
    firstString = "AWS is "
    secondString = "incredible"

    # Writing item
    inputParams = {
        "firstString" : firstString,
        "secondString" : secondString
    } 

    # To invoke a function asynchronously, set InvocationType to Event .
    response = client.invoke(
        FunctionName = "arn:aws:lambda:eu-central-1:524748656081:function:dsg-project-1-dev-calledFunction",
        InvocationType = 'RequestResponse',
        Payload = json.dumps(inputParams)
    )

    # Loading response of called function
    responseFromCalled = json.load(response['Payload'])

    return "This sentence should be same with result! AWS is incredible. Result is : {}.".format(responseFromCalled["Result"])        