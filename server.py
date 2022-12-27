from flask import Flask


#Create the app object that will route our calls
app = Flask(__name__)


# Add a single endpoint that we can use for testing
@app.route('/')
def home():
    return '<h1> Hello World holi</h1><p>My name is Toto</p>'


if __name__== '__main__':
    app.run(host ='0.0.0.0', port = 3333, debug = True)