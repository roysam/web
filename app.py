from flask import Flask

app = Flask(__name__)

#decorator  - route URL "/" to function super_world()
 
@app.route("/")

def super_world():
    return "Hey Juniper"

#decorator - route URL "/hello" to function hello_world()

@app.route("/hello")

def hello_world():
    return "Hello,Junos Automation"

if __name__ == "__main__":
    app.run(host="0.0.0.0")


