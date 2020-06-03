import os
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('CuzvEwcX102lW5EyIJv/BXXixlK6eMl0bXU6QS1RGLZl56dBgMojQj3hFf9xq4dczBZgQokDFG7Lc5gXk16n50QH9BK9r+n3U5iAYq7BF4vNJo8ClchVTLTVQ2cJOFQaus+DVd4Tf7Fcgd/fmYRZGwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('2b68cd064176f3b957dd492aae378a8e')


@app.route("/callback", methods=['POST'])
def callback():
    # Get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # Get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # Handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    """ Here's all the messages will be handled and processed by the program """

    if "hallo" in msg:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=Hello apa kabar?))
    elif "apa kabar" in msg:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=baik, alhamdulillah))
    else :
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
