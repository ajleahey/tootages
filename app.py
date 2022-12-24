import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    timeline_url = 'https://esq.social/api/v1/timelines/public'
    response = requests.get(timeline_url)
    toots = response.json()

    images = []
    for toot in toots:
        for attachment in toot['media_attachments']:
            images.append(attachment['url'])

    return render_template('index.html', images=images)
