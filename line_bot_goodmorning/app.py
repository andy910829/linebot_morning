from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from datetime import datetime

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('36joHO+uKUo/ps1zxTG/tUQ8OJ5RssJ+ikiKIs3IHxEj2Zfi9XbcE7+uP9LCsyM0slHiofkoF1uds67FGtiuUHrIHZNV35MgJeulnmK0iQQmDvjY8XSECxe+HBMtlH20qnVxoh4mbiTlFIdst+69AQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('5321025785448893bcb70824bc21f8eb')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message = TextMessage)
def handle_message(event):
    if event.message.text == 'hi' or event.message.text =='Hi' :
        # group_id = event.source.group_id
        message1 = ImageSendMessage(
        original_content_url='https://memeprod.sgp1.digitaloceanspaces.com/user-wtf/1625032216898.jpg',
        preview_image_url='https://memeprod.sgp1.digitaloceanspaces.com/user-wtf/1625032216898.jpg'
            )
        message2 = ImageSendMessage(
        original_content_url='https://chunting.me/wp-content/uploads/2018/07/OElrPtB.jpg',
        preview_image_url='https://chunting.me/wp-content/uploads/2018/07/OElrPtB.jpg'
        )
        message3 = ImageSendMessage(
        original_content_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQysOM9eqrFQMjN1437DUSEHQrLWsCEXr0a4fnN2WLnZFV08ntI6Wy3FmtzcvjSPc0ort4&usqp=CAU',
        preview_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQysOM9eqrFQMjN1437DUSEHQrLWsCEXr0a4fnN2WLnZFV08ntI6Wy3FmtzcvjSPc0ort4&usqp=CAU'
        )
        message4 = ImageSendMessage(
        original_content_url='https://innews.com.tw/wp-content/uploads/2021/03/129815786_212732853768791_6951417886102725054_o.jpg',
        preview_image_url='https://innews.com.tw/wp-content/uploads/2021/03/129815786_212732853768791_6951417886102725054_o.jpg'
        )
        message5 = ImageSendMessage(
        original_content_url='https://img.ltn.com.tw/Upload/ent/page/800/2020/08/22/3267861_1.jpg',
        preview_image_url='https://img.ltn.com.tw/Upload/ent/page/800/2020/08/22/3267861_1.jpg'
        )
        img = [message1, message2, message3, message4, message5]
        now = int(datetime.now().timestamp())
        random = now % 5
        line_bot_api.reply_message(event.reply_token, img[random])


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
