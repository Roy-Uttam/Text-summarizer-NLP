from flask import Flask, render_template,request
from summarizer import Summarizer
from summarizer.sbert import SBertSummarizer

#create an instance of the SBERT
model = SBertSummarizer('paraphrase-MiniLM-L6-v2')

app = Flask(__name__)

@app.route("/")
def msg():
    return render_template('index.html')

@app.route("/summarize",methods=['POST','GET'])
def getSummary():
    body=request.form['data']
    result = model(body, num_sentences=5)
    return render_template('index.html',result=result,Data=body)

if __name__ =="__main__":
    app.run(debug=True,port=8000)
