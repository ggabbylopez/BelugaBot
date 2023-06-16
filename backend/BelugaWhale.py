import json
from TeamsMessenger import sendMessage

def lambda_handler(event, context):
    update_type = ""
    author = ""
    repository = ""
    if 'headers' in event.keys():
        print(event["headers"])
        if "X-Event-Key" in event["headers"].keys():
            print(event['headers']['X-Event-Key'])
            update_type = event["headers"]["X-Event-Key"]

    if "body" in event.keys():
        print(event["body"])
        author = event["body"]["actor"]
        repository = event["body"]["repository"]

    print("Received notification: {} - {} - {}".format(update_type, author, repository))
    message = "{} Update to {} by {}".format(update_type, repository, author)
    webhook = "https://eaglefgcu.webhook.office.com/webhookb2/5b668ebc-a9f1-4575-990c-888124a9f2df@f7a5a4ef-4ffa-4c80-bfb3-c12e28872099/IncomingWebhook/69a44ccb361a429bb75418702106fef1/2d04b75f-b6a7-4f37-8386-a11f40753184"
    sendMessage(message, webhook)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }