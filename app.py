from backend import get_proposal
from flask import Flask,render_template,jsonify,request

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_proposal",methods=["POST"])
def generate():
    data=request.get_json()
    profile_description=data["profile_description"]
    job_desctiption =data["job_description"]
    response=get_proposal(profile_description,job_desctiption)
    return jsonify({"response":response})

if __name__ == "__main__":
    app.run(debug=True)