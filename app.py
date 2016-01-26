from flask import Flask

app = Flask(__name__)

#Enable automatic config changes reload
app.config["DEBUG"] = True

#decorator  - route URL "/" to function super_world()
 
@app.route("/")

def super_world():
    return "Hey Juniper"

#decorator - route URL "/hello" to function hello_world()

@app.route("/hello")

def hello_world():
    return "Hello world,Junos Automation"

#Dynamic Route
@app.route("/test/<search_query>")

def search(search_query):
    message = "This is the input: " + search_query    
    return message

@app.route("/integer/<int:value>")

def int_type(value):
    value += 1
    return "Incremented: " + str(value)

@app.route("/directory/<path:value>")

def vm_directory(value):
    return "Repository: " + value

@app.route("/name/<name>")

def find_contact(name):
    if name.lower() == "juniper":
        return "Hello Juniper Networks"
    else:
        return "Unknown Tech Company", 404




if __name__ == "__main__":
    app.run(host="0.0.0.0")


