import json

from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

Database_file = './messenger/data/datbase.json' # this path is for my pc
db = open(Database_file, "rb")  # rb means for reading
data_mes = json.load(db)
messages = data_mes['messages']  # from data we got, we take the messages field


def save_messages_to_file():
    db = open(Database_file, "w")
    data_mes = {
        'messages': messages
    }
    json.dump(data_mes, db)


# main page
@app.route('/')
def index_page():
    return 'Greetings, man!'


# show all messages in json
@app.route('/get_messages')
def get_messages():
    return {'messages': messages}


@app.route('/send_message')
def send_message():
    name = request.args['name']
    text = request.args['text']
    add_message(text, name)
    return 'ok'


def print_message(message):
    print(f"[{message['sender']}]:{message['time']} /{message['text']}")


def add_message(text, sender):
    now = datetime.datetime.now()
    new_message = {
        'text': text,
        'sender': sender,
        'time': now.strftime('%d-%m-%Y %H:%M')
    }
    messages.append(new_message)
    save_messages_to_file()


@app.route('/form')
def form():
    return render_template('/form.html')


app.run()  # app.run("host=0.0.0.0", port=80)
