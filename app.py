from flask import Flask, jsonify, request, render_template
from answer import Answer
from collect import Collect
import re
regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

answers = Answer()
collecting = Collect()
app = Flask(__name__) 
  
@app.route('/', methods = ['POST']) 
def home(): 
    if(request.method == 'POST'): 
        data = request.get_json()
        reply = answers.getReply(data['q'])
        return jsonify({'answer': reply}) 

@app.route("/page")
def page():
    return render_template("page.html")

@app.route('/url', methods = ['POST']) 
def url():
    if(request.method == 'POST'):
        data = request.get_json()
        if(re.match(regex, data['url']) is not None):
            # print(re.match(regex, data['url']) is not None)
            result = collecting.do(data['url'])
            return jsonify({'success': True, 'data': result})
        else:
            return jsonify({'success': False, 'error': 'url malformed...'})

if __name__ == '__main__': 
    app.run(debug = True, port=5656, threaded=False) 
