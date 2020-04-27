from flask import Flask, jsonify, request 
from answer import Answer

answers = Answer()
app = Flask(__name__) 
  
@app.route('/', methods = ['POST']) 
def home(): 
    if(request.method == 'POST'): 
        data = request.get_json()
        reply = answers.getReply(data['q'])
        return jsonify({'answer': reply}) 

if __name__ == '__main__': 
    app.run(debug = True, port=5656, threaded=False) 
