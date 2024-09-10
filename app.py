from flask import Flask

app = Flask(__name__)

@app.route("/")
def hell_world():
  return "hello world"

@app.route("/about")
def about():
  return "Sobre a pagin"

if __name__ == "__main__":
  app.run(debug=True)