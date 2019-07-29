from bot import telegram_chatbot


bot = telegram_chatbot("config.cfg")


def make_reply(msg):
    reply = "okay"
    return reply

def make_reply1(greet):
    reply1 = 'how may i help you'
    return reply1





update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            reply1 = make_reply1(message)
            bot.send_message(reply, from_)
            bot.send_message(reply1, from_)
