
from flask import *         #importing all functions
from flask_mysqldb import MySQL
import os
from werkzeug.utils import secure_filename
import numpy as np
import pickle
from werkzeug.utils import secure_filename




app = Flask(__name__)
mysql= MySQL(app)
#database conflig
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='granite'
#pkl file 
model = pickle.load(open("model.pkl", "rb"))
#image insert
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = 'static/img'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#main page
@app.route("/")
def hello_world():
    
    return render_template('outlier.html')

@app.route("/portfolio1")
def portfolio1():
    return render_template('portfolio1.html')

@app.route("/portfolio_submit", methods=['POST','GET'])
def portfolio_1():
    if request.method== 'POST':
        cursor=mysql.connection.cursor()
        name= request.form['name']
        dob= request.form['dob']
        email= request.form['email']
        mobno= request.form['mobno']
        gen= request.form['gen']
        occ= request.form['occ']
        hobby= request.form['hobby']       
        pro_nam= request.form['pro_nam']
        com_nam= request.form['com_nam']
        nation= request.form['nation']
        
        address= request.form['address']
        session['name']=name        #session
        file = request.files['img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))       
        sql="INSERT INTO `portfolio`(`name`, `email`, `dob`, `gen`, `occ`, `hobby`, `pro_name`, `ph_no`, `coun`, `img`,`com_name`,`address`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        value=[name,email,dob,gen,occ,hobby,pro_nam,mobno,nation,filename,com_nam,address]
        cursor.execute(sql,value)
        mysql.connection.commit()
        return redirect('/portfolio2')
    return render_template('portfolio1.html')

@app.route("/portfolio2")
def portfolio2():
    return render_template('portfolio2.html')
@app.route("/sidebar")
def sidebar():
    return render_template('sidebar.html')

@app.route("/portfolio2_submit", methods=['POST','GET'])
def portfolio_2():
    if request.method== 'POST':
        cursor=mysql.connection.cursor()
        sname1= request.form['sname1']
        year1= request.form['year1']
        marks1= request.form['marks1']
        sname2= request.form['sname2']
        year2= request.form['year2']
        marks2= request.form['marks2']
        cname1= request.form['cname1']
        year3= request.form['year3']
        marks3= request.form['marks3']
        cname2= request.form['cname2']
        year4= request.form['year4']
        marks4= request.form['marks4']
        sql="UPDATE `portfolio` SET  `sname1`=%s, `year1`=%s, `marks1`=%s, `sname2`=%s, `year2`=%s, `marks2`=%s, `cname1`=%s, `year3`=%s, `marks3`=%s, `cname2`=%s, `year4`=%s, `marks4`=%s WHERE `name`=%s"
        value=[sname1,year1,marks1,sname2,year2,marks2,cname1,year3,marks3,cname2,year4,marks4,session['name']]
        cursor.execute(sql,value)
        mysql.connection.commit()
        return redirect('/portfolio3')
    return render_template('portfolio2.html')



@app.route("/portfolio3")
def portfolio3():
    return render_template('portfolio3.html')

@app.route("/portfolio3_submit", methods=['POST','GET'])
def portfolio_3():
    if request.method== 'POST':
        cursor=mysql.connection.cursor()
        skills= request.form['skills']
        front= request.form['front']
        back= request.form['back']
        interest= request.form['interest']
        activity= request.form['activity']
        obj= request.form['obj']
        course= request.form['course']
        experience= request.form['experience']      
        sql="UPDATE `portfolio` SET `programming_skills`=%s, `frontend`=%s, `backend`=%s, `sub_int`=%s, `career_objectives`=%s, `courses`=%s, `exp`=%s, `activity`=%s WHERE `name`=%s"
        value=[skills,front,back,interest,obj,course,experience,activity,session['name']]
        cursor.execute(sql,value)
        mysql.connection.commit()
        return redirect('/resume')
    return render_template('portfolio2.html')

#Fetching Resume
@app.route("/resume")
def resume():
    cur= mysql.connection.cursor()
    sql= "SELECT * FROM `portfolio` ORDER BY ID DESC LIMIT 1"
    
    fetch_data= cur.execute(sql)
    fetch= cur.fetchall()


    return render_template('cv(1).html',fetch=fetch)

@app.route("/demo")
def demo():
    return render_template('cv.html')

#Prediction form page
@app.route("/pred")
def pred():
    return render_template('form.html')

#Prediction form page
@app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    return render_template("form.html", prediction_text = "You shoud learn {}".format(prediction))

#Login page
@app.route("/login")
def login():
    return render_template('login.html')

#Submit login page
@app.route("/loginsubmit", methods=['POST','GET'])
def login_submit():
    if request.method== 'POST':
        cursor=mysql.connection.cursor()
        det= request.form
        username= request.form['username']
        password= request.form['password']
        sql="SELECT * FROM `user` WHERE `user_name`=%s and `user_password`=%s"
        values=[username,password]
        cursor.execute(sql,values)
        record=cursor.fetchone()
        if record:
            session['username']=record[1]   #creating session
            return render_template('outlier.html')
        else:       
            msg='Invalid username and password!!'
            return render_template('login.html', msg=msg)
    else:
        msg='Invalid username and password!!'
        return render_template('login.html', msg=msg)

        



#Sign in page
@app.route('/signin')
def signin():
    return render_template('signin.html')

#Submit Singin page
@app.route("/create_user", methods=['POST','GET'])
def create_user():
    
    if request.method=="POST":
        cursor= mysql.connection.cursor()
        details= request.form
        name= request.form['name']
        email= request.form['email']
        password= request.form['password']
        sql="INSERT INTO `user`(`user_name`, `user_password`, `user_email`) VALUES (%s,%s,%s)"
        value=[name,password,email]
        cursor.execute(sql,value)
        mysql.connection.commit()
    return render_template('outlier.html')






# About Page
@app.route("/about")
def about():
    return render_template('about.html')

#Help page
@app.route("/help")
def help():
    return render_template('help.html')


@app.route("/cv")
def cv():
    return render_template('cv.html')
@app.route("/tech")
def tech():
    return render_template('technology.html')







if __name__== '__main__':
    app.secret_key="Super secret key"       #Secret key for session
    app.config['SESSION_TYPE']='filesystem'
    app.run(debug=True)
    