from flask import Flask, render_template, flash, redirect, url_for, session, request, logging


app = Flask(__name__)

# Index
@app.route('/')
def index():
    return render_template('home.html')




    
if __name__ == '__main__':
    app.run(debug=True)