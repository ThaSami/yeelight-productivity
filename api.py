from flask import Flask, jsonify, request
import time
from yeelight import Bulb

app = Flask(__name__)
banned_urls = ['facebook', 'youtube', 'twitter', 'whatsapp']
bulb = Bulb("YEELIGHT-IP-ADDRESS")
current_state = "productive"


def url_strip(url):
    if "http://" in url or "https://" in url:
        url = url.replace("https://", '').replace("http://", '').replace('\"', '')
    if "/" in url:
        url = url.split('/', 1)[0]
    return url


@app.route('/send_url', methods=['POST'])
def send_url():
    resp_json = request.get_data()
    params = resp_json.decode()
    url = params.replace("url=", "")
    print("currently viewing: " + url_strip(url))
    parent_url = url_strip(url)

    if any(url in parent_url for url in banned_urls):
        bulb.set_rgb(255, 0, 0)
        global current_state
        current_state = "NoTPRODUCTIVE"
    else:
        if current_state != "productive":
            bulb.set_color_temp(4700)
            current_state = "productive"

    return jsonify({'message': 'success!'}), 200


app.run(host='0.0.0.0', port=5000)
