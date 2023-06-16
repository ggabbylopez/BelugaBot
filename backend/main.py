import json
from fastapi import FastAPI, Request
from TeamsSender import SendMessage
from bitbucket_webhooks import event_schemas, hooks, router

app = FastAPI()


@app.post("/webhook/bitbucket")
def bitbucket(st: str):
    event = json.loads(st)
    update_type = ""
    author = ""
    repository = ""
    link = "https://bitbucket.org/belugabottester/belugabottester/src/main/"
    if 'headers' in event.keys():
        print(event["headers"])
        if "X-Event-Key" in event["headers"].keys():
            print(event['headers']['X-Event-Key'])
            update_type = event["headers"]["X-Event-Key"]

    if "body" in event.keys():
        print(event["body"])
        author = event["body"]["actor"]
        repository = event["body"]["repository"]

    print("Received notification: {} - {} - {}".format(update_type, author, repository, link))
    message = "A {} to {} was made by {} at {}".format(update_type, repository, author, )
    webhook = "https://eaglefgcu.webhook.office.com/webhookb2/5b668ebc-a9f1-4575-990c-888124a9f2df@f7a5a4ef-4ffa-4c80-bfb3-c12e28872099/IncomingWebhook/69a44ccb361a429bb75418702106fef1/2d04b75f-b6a7-4f37-8386-a11f40753184"
    SendMessage(message, webhook)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
@app.post("/webhook")
def bitbucket(action: str, author: str, repository: str):
        
    link = "https://bitbucket.org/belugabottester/belugabottester/src/main/"
    print("Received notification: {} - {} - {}".format(action, author, repository))
    message = "{} to {} was made by {} at {}".format(action, repository, author, link)
    webhook = "https://eaglefgcu.webhook.office.com/webhookb2/5b668ebc-a9f1-4575-990c-888124a9f2df@f7a5a4ef-4ffa-4c80-bfb3-c12e28872099/IncomingWebhook/69a44ccb361a429bb75418702106fef1/2d04b75f-b6a7-4f37-8386-a11f40753184"
    SendMessage(message, webhook)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }