from flask import Flask, render_template, request

from src import zigu_fees



#Create the app object that will route our calls
app = Flask(__name__)

# Add a single endpoint that we can use for testing
@app.route('/', methods=['GET','POST'])
def home():
    transaction = ((0),(0))
    if request.method == "POST":        
        transaction = zigu_fees(float(request.form.get("amount")))
    return render_template('index.html', result=transaction)


if __name__== '__main__':
    app.run(debug = True)
