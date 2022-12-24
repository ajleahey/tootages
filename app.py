import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    timeline_url = 'https://esq.social/api/v1/timelines/public'
    headers = {
        'Authorization': 'Bearer oTx3JC-FgLqQpwWXMytb67PC_RazSuxeFB14N8JbrPQ'
    }
    params = {
        'limit': 100
    }
    response = requests.get(timeline_url, headers=headers, params=params)
    toots = response.json()

    images = []
    handles = []
    captions = []
    for toot in toots:
        for attachment in toot['media_attachments']:
            images.append(attachment['url'])
            handles.append(toot['account']['acct'])
            captions.append(toot['content'])

    return render_template('index.html', images=images, handles=handles, captions=captions)

