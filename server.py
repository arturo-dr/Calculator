from flask import Flask, render_template


#Create the app object that will route our calls
app = Flask(__name__)


# Add a single endpoint that we can use for testing
@app.route('/')
def home():
    return render_template('home.html')


if __name__== '__main__':
    app.run(host ='0.0.0.0', port = 3333, debug = True)