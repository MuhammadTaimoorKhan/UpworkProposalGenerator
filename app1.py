from backend import get_proposal
from flask import Flask,render_template,jsonify,request
 
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index1.html")

@app.route("/get_proposal",methods=["POST"])
def genarate():
    data=request.get_json()
    profiledescription=data["profiledescription"]
    job_Description =data["job_Description"]
    response=get_proposal(profiledescription,job_Description)
    return jsonify({"response":response})

if __name__=="__main__":
    app.run(debug=True)