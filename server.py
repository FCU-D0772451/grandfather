from flask import Flask, request, make_response, jsonify

import pyimgur
from imgurpython import ImgurClient
import random



## heruko
def morning():

    r = random.randrange(0, 6)
    print(r)

    client = ImgurClient('07f717179f3bd69', 'f3e15f93b6e66c05aff4f91b2b2f7519d2bc1eb3')
    items = client.get_album_images('NzTojyH')

    '''
    client_id = '51503dac7c6d0b9'
    path = '早安/' + '長輩圖 ' + '(' + str(r) + ')' + '.jpg'

    im = pyimgur.Imgur(client_id)
    upload_image = im.upload_image(path)
    '''

    return items[r].link



def afternoon():

    r = random.randrange(0, 7)
    print(r)

    client = ImgurClient('07f717179f3bd69', 'f3e15f93b6e66c05aff4f91b2b2f7519d2bc1eb3')
    items = client.get_album_images('QuqQLOK')

    '''
    client_id = '51503dac7c6d0b9'
    path = '午安/' + '長輩圖 ' + '(' + str(r) + ')' + '.jpg'

    im = pyimgur.Imgur(client_id)
    upload_image = im.upload_image(path)
    '''

    return items[r].link

def goodnight():

    r = random.randrange(0, 7)
    print(r)
    
    client = ImgurClient('07f717179f3bd69', 'f3e15f93b6e66c05aff4f91b2b2f7519d2bc1eb3')
    items = client.get_album_images('xLshDgQ')

    '''
    client_id = '07f717179f3bd69'
    path = '晚安/' + '長輩圖 ' + '(' + str(r) + ')' + '.jpg'

    im = pyimgur.Imgur(client_id)
    upload_image = im.upload_image(path)
    '''

    return items[r].link


def hell():

    r = random.randrange(0, 7)
    print(r)

    client = ImgurClient('07f717179f3bd69', 'f3e15f93b6e66c05aff4f91b2b2f7519d2bc1eb3')
    items = client.get_album_images('iJ2Vho3')

    '''
    client_id = '07f717179f3bd69'
    path = '地獄/' + '地獄 ' + '(' + str(r) + ')' + '.jpg'


    im = pyimgur.Imgur(client_id)
    upload_image = im.upload_image(path)
    '''

    return items[r].link


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])

def webhook():
    json = request.get_json(silent=True,force=True)

    res_message = {"fulfillmentText": None}
    
    if json['queryResult']['parameters']['any'] == "菜單":
        msg = ""
        msg += "以下為所有功能:\n"
        msg += "輸入 早安\n"
        msg += "輸入 午安\n"
        msg += "輸入 晚安\n"
        msg += "輸入 地獄\n"
        
        res_message = {"fulfillmentMessages": [ { "text": { "text": [msg] } } ] }

    elif json['queryResult']['parameters']['any'] == "早安":
    
        msg = morning()
        res_message =   {"fulfillmentMessages" : [ {"image" : { "imageUri" : msg } } ] } 


    elif json['queryResult']['parameters']['any'] == "地獄":
    
        msg = hell()
        res_message =   {"fulfillmentMessages" : [ {"image" : { "imageUri" : msg } } ] } 


    elif json['queryResult']['parameters']['any'] == "午安":
    
        msg = afternoon()
        res_message =   {"fulfillmentMessages" : [ {"image" : { "imageUri" : msg } } ] } 
    
    elif json['queryResult']['parameters']['any'] == "晚安":
    
        msg = goodnight()
        res_message =   {"fulfillmentMessages" : [ {"image" : { "imageUri" : msg } } ] } 

    return make_response(jsonify(res_message))


if __name__ == "__main__":
    app.run(port=5000)