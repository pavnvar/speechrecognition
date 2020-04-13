from flask import Flask,render_template,url_for
from flask import request
app=Flask(__name__)

@app.route("/")
def home():
    print("home page")
    return render_template('home.html')
@app.route("/get-speech-value",methods=["GET","POST"])
def get_speech():
    if (request.method=="POST"):
        try:
            print("received a post request from",request)
            print("the content is",request.form.get('name'))
            return {"msg": "success"}, 202
        except Exception as e:
            return {"msg": e}, 404
if __name__=='__main__':
    app.run(debug=True,host="127.0.0.1")

