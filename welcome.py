from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "<h1> Welcome to your new office! This image will be sent to docker hub! Deployed on Kubernetes on AWS. V5, Date: 21.10.2022 / 10:55  </h1> "
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
