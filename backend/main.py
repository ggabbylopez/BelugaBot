import json
from fastapi import FastAPI, Request
from decouple import config
from TeamsSender import SendMessage

app = FastAPI()


@app.post("/webhook/pullRequest")
async def handle_pr(request: Request):
    json_obj = await request.json()
    message = "{} opened a pull request to merge ({} -> {})" \
              "\nLink to PR: {}".format(
        json_obj["actor"]["display_name"],
        json_obj["pullrequest"]["source"]["branch"]["name"],
        json_obj["pullrequest"]["destination"]["branch"]["name"],
        json_obj["pullrequest"]["links"]["html"]["href"])

    webhook = config('WEBHOOK')
    SendMessage(message, webhook)
    return {
        'statusCode': 200,
        'body': json.dumps('Ok!')
    }


@app.post("/webhook/pullRequestUpdated")
async def handle_pr_update(request: Request):
    json_obj = await request.json()
    message = "{} has updated a pull request ({})" \
              "\nLink to PR: {}".format(
        json_obj["actor"]["display_name"],
        json_obj["pullrequest"]["title"],
        json_obj["pullrequest"]["links"]["html"]["href"])

    webhook = config('WEBHOOK')
    SendMessage(message, webhook)
    return {
        'statusCode': 200,
        'body': json.dumps('Ok!')
    }


@app.post("/webhook/pullRequestApproved")
async def handle_pr_approval(request: Request):
    json_obj = await request.json()
    message = "{} has approved a pull request ({})" \
              "\nLink to PR: {}".format(
        json_obj["actor"]["display_name"],
        json_obj["pullrequest"]["title"],
        json_obj["pullrequest"]["links"]["html"]["href"])

    webhook = config("WEBHOOK")
    SendMessage(message, webhook)
    return {
        'statusCode': 200,
        'body': json.dumps('Ok!')
    }


@app.post("/webhook/pullRequestMerged")
async def handle_pr_merge(request: Request):
    json_obj = await request.json()
    message = "{} has merged a pull request ({})" \
              "\nLink to PR: {}".format(
        json_obj["actor"]["display_name"],
        json_obj["pullrequest"]["title"],
        json_obj["pullrequest"]["links"]["html"]["href"])

    webhook = config('WEBHOOK')
    SendMessage(message, webhook)
    return {
        'statusCode': 200,
        'body': json.dumps('Ok!')
    }


@app.post("/webhook/pullRequestCommented")
async def handle_pr_commented(request: Request):
    json_obj = await request.json()
    message = "{} has commented on a pull request ({})" \
              "\nLink to PR: {}".format(
        json_obj["actor"]["display_name"],
        json_obj["pullrequest"]["title"],
        json_obj["pullrequest"]["links"]["html"]["href"])
    webhook = config('WEBHOOK')
    SendMessage(message, webhook)
    return {
        'statusCode': 200,
        'body': json.dumps('Ok!')
    }