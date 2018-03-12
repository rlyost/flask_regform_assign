from flask import Flask, render_template, redirect, request, session, flash
import re 
import datetime
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
  session['dob'] = request.form['birth']
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
    elif str.islower(str(session['password'])):
      flash("Your password must have at least one Uppercase character and one Lowercase character")
      return redirect('/')
    elif session['password'] != session['password2']:
      flash("Passwords do not match, try again!")
      return redirect('/')
  else:
    print session['fname'], session['lname']
    flash("First and/or Last Name can not be empty or contain numbers!")
    return redirect('/')

  try:
    print str(session['dob'])
    datetime.datetime.strptime(str(session['dob']), '%Y-%m-%d')
  except ValueError:
    raise ValueError("Incorrect data format, should be YYYY-MM-DD")
    return redirect('/')
  if datetime.datetime.now() < datetime.datetime.strptime(str(session['dob']), '%Y-%m-%d'):
    flash("Date of Birth not possible, try again!")
    return redirect('/')
  
  flash("SUCCESS!!!!")
  return redirect('/')
  

app.run(debug=True)
