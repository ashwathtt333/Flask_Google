# Importing flask module , rendder template to open html page , request to grab arguments from the inputs
from flask import Flask, render_template, request
app = Flask(__name__)
# This page will have the sign up form
@app.route('/')
def signup_form():
    return render_template('signup.html')

# This page will be thank you form displaying the names you entered in the html document.
@app.route('/thankyou')
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('thanks.html',first=first,last=last) #Grabbing the name='first and name='second' from the sign up html document through request 
if __name__ == '__main__':
    app.run(debug=True)
