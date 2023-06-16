import json
from fastapi import FastAPI, Request
from decouple import config
from TeamsSender import SendMessage

app = FastAPI()

@app.post("/webhook/bitbucket")
async def bitbucket(request: Request):
    json_obj = await request.json()
    message = "{} has made a pull request ({}) in repo {}".format(json_obj["actor"]["display_name"], json_obj["pullrequest"]["title"], json_obj["repository"]["links"]["html"]["href"])

    webhook = config('WEBHOOK')
    SendMessage(message, webhook)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }