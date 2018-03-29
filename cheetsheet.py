

#PYTHON CHEETSHEET


#important libraries
from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

#PRERQUISTICS
>HTML FILES SHOULD BE IN TEMPLATE FOLDER 
>REST FILES,CSS,JS,IAGES SHOULD BE I STATIC FOLDER
>FOR LLINKING PAGES OR THINGS IN HTML,USE URL FOR().
ie  <link href="{{ url_for('static', filename='css/bootstrap-theme.min.css') }}" rel="stylesheet">
	<link href="{{ url_for('static', filename='css/bootstrap.min.css') }}" rel="stylesheet"> 
    <form action="{{url_for('success')}}" method="POST">
>SYNTAX::  from flask import Flask, render_template

            app=Flask(__name__)

            @app.route('/')
            def home():
			return render_template('index.html')
			
    return render_template("home.html")
            if __name__=="__main__":
            app.run(debug=True)

       

#Setting connection with our database(between website and database)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/height_collector' //postgresql://username:password@localhost or website address/database name
db=SQLAlchemy(app)#creating db object of our app


#Grab data from form and storing it in variable
	email=request.form[email_name]
	password=request.form[password_name]
	
#Printing grabbed data
print(email)
print(password)


#Saving grabbed data in database
#CREATE A TABLE [table is called modle in python] in our database
#db object bna of class data
class Data(db.Model):
    __tablename__="data" #name of table
    id=db.Column(db.Integer, primary_key=True)#ID naam ka ek column.Ye automatic update hota rehta hai
    email=db.Column(db.String(120), unique=True) #Email naam ka ek column
    password=db.Column(db.Integer) #height naam ka ek column

	
	#Initialize all columsn
    def __init__(self, email_, height_):
        self.email_=email_
        self.height_=height_
		
#linking local host to database of pgadmin so that it will start working as i enter something in form offline
python app.py
from app import db 
db.create_all()

	
#Printing database on webpage

#create one Div/Table's column.Loop it so that whenever new data is added,it appends same div
	{% for r in result %}
	<div>
		<div class="col-md-4">{{r.email}}</div>
		<div class="col-md-4">{{r.password}}</div>
	</div>
	{% endfor %}

	
#using loops:
#for loop
{% for r in result %}
{% endfor %}
#if esle
{% if myvar%}
	....
{% else %}
	...
{% endif %}

#USING VARIABLES IN HTML
<div>this is variable {{myvar}}</div>
how to use?
In app.py ie When returning html page in rendertemplatemethod declare myvar
def index():
    return render_template("index.html",myvar="this will be variable")
	

#LINKING HTML WITH PYTHON  (ROUTING)
first there will be index page.ie /. ie www.index.com/
@app.route('/')
def index():
	return render_template('index.html')
	
#MISC ON ROUTING
	@app.route('/',method=['GET','POST'])#you can write which method you want when going from one page to another
	def index():
	return render_template('index.html',myvar=email)#you can pass variables here
	
#INTERLINKING PAGES IN PYTHON
if you want that when clicking this link,you should  be redirected to About page lets say.
use {{url for('')}} in the html page
<a href="{{ url_for('about') }}">About page</a>
and create a route for this in app.py
ie,
@app.route('/about')
def aboutpage():
    return render_template("aboutpage.html")
	
#REDIRECTING TO A PARTICULAR PAGE
@app.route('/process', methods=['POST'])
def process():
	name = request.form['name']
	comment = request.form['comment']

	signature = Comments(name=name, comment=comment)
	db.session.add(signature)
	db.session.commit()
	return redirect(url_for('index'))
	
#Note::
Jo table create karne wali process hai,use @app.route(/process) dede.
Fir iske funcction me table creation ka code likh
and if iske baad if you want to go to some page then return render_template()
or if you want to go to index page with refreshed updated data-use redirect
return redirect(url_for('index'))
And,form ke action ko process ka naam dedo.        
ie..<form action="{{url_for('process')}}" method="POST">
          <input title="Your email will be safe with us"  type="email" name="email_name" required> <br>
          <input title="Your data will be safe with us"  name="height_name" required> <br>
          <button type="submit"> Submit </button>
    </form>