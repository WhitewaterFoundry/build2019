from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hello Build 2019! Visit pengwin.dev/build2019 for more."
 
if __name__ == "__main__":
    app.run()