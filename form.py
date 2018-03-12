from flask import Flask, render_template, redirect, request, session, flash
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'RangersLeadtheWay'
@app.route('/')
def index():
  return render_template('index.html')
@app.route('/process', methods=['POST'])
def process():
  session['email'] = request.form['email']
  session['fname'] = request.form['fname']
  session['lname'] = request.form['lname']
  session['password'] = request.form['password']
  session['password2'] = request.form['password2']
  
  if len(session['email']) < 1:
        flash("Email cannot be blank!")
        return redirect('/')
  elif not EMAIL_REGEX.match(session['email']):
        flash("Invalid Email Address!")
        return redirect('/')
  if str.isalpha(str(session['fname'])) and str.isalpha(str(session['lname'])):
    if len(session['password']) < 9:
      flash("Password is not long enough")
      return redirect('/')
    elif session['password'] != session['password2']:
      flash("Passwords do not match, try again!")
      return redirect('/')
  else:
    print session['fname'], session['lname']
    flash("First and/or Last Name can not be empty or contain numbers!")
    return redirect('/')
  flash("SUCCESS!!!!")
  return redirect('/')
app.run(debug=True)
