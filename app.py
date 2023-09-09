from flask import Flask, render_template, request
import urllib.request, json

url = "https://xkcd.com/info.0.json"
response = urllib.request.urlopen(url)
data = response.read()
dict = json.loads(data)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", datum=dict)

@app.route("/about")
def about():
    name = request.arg.get('name') if request.args.get('name') else "Hello World!" 
    return render_template("about.html", aboutName=name)

@app.route("/<name>")              
def hello_name(name):              
    return "Hello "+ name   

if __name__ == "__main__":
    app.run(debug=True)