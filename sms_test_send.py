from twilio.rest import Client


def sendtext(message):
    client = Client('AC523b8a138eea899153da4562c8d92f48', '88b5fbae4fd61a9c5a97936924eda4be')
    client.messages.create(to = "+15153600909",
                       from_ = "15156195346",
                       body = message)
