from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    print(f"New message received:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Message: {message}")

    # In real app, you can send email or save to database here

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
