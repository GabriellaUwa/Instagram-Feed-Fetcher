from flask import Flask
import urllib2, xmltodict, json
from io import BytesIO

app = Flask(__name__)

@app.route('/pinterest_feeds')
def pinterest_feed(username="ipsy", boardname=None):

    if boardname is None:
        file = urllib2.urlopen('https://www.pinterest.com/'+username+'/feed.rss')
    else:
        file = urllib2.urlopen('https://www.pinterest.com/'+username+'/' + boardname +'.rss')

    data = file.read()
    file.close()

    data = xmltodict.parse(data)

    return app.response_class(BytesIO(json.dumps(json.loads(json.dumps(data)))), content_type='application/json')

if __name__ == '__main__':
    app.run()

#TODO: Will be implemented differently. This only gets publicly allowed pins