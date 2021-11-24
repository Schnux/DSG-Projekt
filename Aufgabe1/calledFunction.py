import json


def concatinateSentence(event, context):
    #1 Reading Parameters:
    firstPart = event['firstString']
    secondPart = event['secondString']

    #2 Final result  
    result = firstPart + secondPart

    return{
        'Result' : result
    }