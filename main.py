from flask import Flask, render_template
from login_form import LoginForm

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
app.secret_key = "jsaoiufjlksjerioqw3jlkrfjsdk"

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    login_form = LoginForm()
    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
