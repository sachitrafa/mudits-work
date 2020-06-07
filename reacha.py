from flask import Flask,render_template 
from forms import RegistrationForm,LoginForm
app= Flask (__name__)

app.config['SECRET_KEY']='vasu'

@app.route("/")
def hello():
	return render_template('index.html')
@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/Volunteer")
def Volunteer():
	form = RegistrationForm()
	return render_template('volunteer.html',title='Volunteer',form=form)
@app.route("/login")
def login():
	return render_template('Login.html',title="Login",form=form)
@app.route("/vision")
def vision():
	return render_template('beliefs.html')

if __name__ == '__main__':
	app.run(debug=True)