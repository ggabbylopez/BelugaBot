import pymsteams

def SendMessage(message, TeamChatWebhook):
    TeamChat = pymsteams.connectorcard(TeamChatWebhook)
    TeamChat.text(message)
    TeamChat.send()

    print("message was successfully sent!")