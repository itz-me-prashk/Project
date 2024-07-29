#2ND Project  
#---------------------------------------------------------------------
import flask
from flask import Flask,render_template,url_for,redirect,request,flash
import flask_mysqldb
from flask_mysqldb import MySQL

#---------------------------------------------------------------------


app=Flask(__name__)

#---------------------------------------------------------------------




app.secret_key = 'Prask'

#MYSQL--CONECTION
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'prasham'
app.config['MYSQL_DB'] = 'project'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_CURSORCLASS']="DictCursor"
mysql = MySQL(app)

#---------------------------------------------------------------------


ADMIN_ID={'Prasham':'LK121'}
#--------------------------------------------------------------------

RUN=0
IDS_USER=0
XFACTOR=False
#---------------------------------------------------------------------



#---------------------------------------------------------------------



@app.route('/note',methods=['GET','POST'])
def home():
    global XFACTOR
    if request.method=='POST' :
        
        title1=request.form['input_title']
        content1=request.form['input_des']
        #---------------------------------------------------------------------
        con=mysql.connection.cursor()
        syn=f'insert into USER{IDS_USER} (TITLE , CONTENT) values(%s,%s)'
        #---------------------------------------------------------------------
        qry=[title1,content1]
        con.execute(syn,qry)
        mysql.connection.commit()
        con.close()
    #---------------------------------------------------------------------
    con=mysql.connection.cursor()
    sql=f'select * from USER{IDS_USER} '
    con.execute(sql)
    result=con.fetchall()
    #---------------------------------------------------------------------
    if XFACTOR==True:
        
        return render_template('index.html',datas=result)
        #---------------------------------------------------------------------
    else:
        return redirect(url_for('signin'))
        #---------------------------------------------------------------------

#---------------------------------------------------------------------
@app.route('/delnote/<string:id>',methods=['POST','GET'])
def delnote(id):
    global XFACTOR
    if XFACTOR==True:
        con=mysql.connection.cursor()
        syn = f'delete from USER{IDS_USER} where ID = %s'
        con.execute(syn,[id])
        mysql.connection.commit()
        con.close()
        return redirect(url_for('home'))
    else:
        return redirect(url_for('signin'))


#---------------------------------------------------------------------
@app.route('/edit/<string:id>',methods=['POST','GET'])


def edit(id):
    
    if request.method=='POST' :
        title1=request.form['input_title1']
        content1=request.form['input_des1']
    #---------------------------------------------------------------------    
        
        con=mysql.connection.cursor()
        syn = f'update USER{IDS_USER} set TITLE = %s,CONTENT = %s where ID= %s'
        qry=[title1,content1,id]
        con.execute(syn,qry)
        mysql.connection.commit()
        con.close()
        return redirect(url_for('home'))
        
    con=mysql.connection.cursor()
    sql=f'select * from USER{IDS_USER} where ID=%s '
    con.execute(sql,[id])
    result2=con.fetchone()
    if XFACTOR:
        return render_template('edithpage.html',datas1=result2)
    else:
        return redirect(url_for('signin'))
    #---------------------------------------------------------------------    
        
    
    
    
    
    #---------------------------------------------------------------------
    
    

#---------------------------------------------------------------------
@app.route('/signin',methods=['POST','GET'])

def signin():
    global IDS_USER
    global XFACTOR
    global RUN
    if request.method == 'POST' :
        username = request.form['username']
        password = request.form['password']
        #---------------------------------------------------------------------
        con=mysql.connection.cursor()
        if username in ADMIN_ID and ADMIN_ID[username]==password:
            
            XFACTOR=True
            flash('Welcome Back ')
            if IDS_USER==0:
                return redirect(url_for('home'))
            else:
                
                IDS_USER=0
                return redirect(url_for('home'))
            
            
        #---------------------------------------------------------------------
        else:
            syn='select*from user_detail where Username=%s and Password = %s'
            
            con.execute(syn,[username,password])
            
            result=con.fetchone()
        #---------------------------------------------------------------------    
            
            
            
            if result: 
               
                XFACTOR=True
                RUN=0
                flash('Welcome Back ')
                
                
                IDS_USER=result['ID']
                return redirect(url_for('home'))
        #---------------------------------------------------------------------
            else:
                flash('User Details Not Found ')
                return redirect(url_for('signup'))
    if XFACTOR==False or RUN==1:    #---------------------------------------------------------------------
        return render_template('none/sign.html')    
    else:
        return redirect(url_for('home'))
    
    
#---------------------------------------------------------------------    
@app.route('/signup',methods=['POST','GET'])

def signup():
    global XFACTOR
    global RUN
    XFACTOR==False
    global IDS_USER
    if request.method == 'POST' :
        username1 = request.form['username1']
        password1 = request.form['password1']
        con=mysql.connection.cursor()
        #---------------------------------------------------------------------
        syn=f'select*from user_detail where Username=%s and Password = %s'
        con.execute(syn,[username1,password1])
        resultx=con.fetchone()
        #---------------------------------------------------------------------
        if username1 in ADMIN_ID  and ADMIN_ID[username1]==password1 :
            
            XFACTOR = True
            flash('Your Already An USER')
            return redirect(url_for('home'))
        #---------------------------------------------------------------------
        elif resultx :
            XFACTOR = True
            flash('Your Already An USER')
            syn=f'select*from user_detail where Username=%s and Password = %s'
            con.execute(syn,[username1,password1])
            resultxx=con.fetchone()
            global IDS_USER
            IDS_USER=resultxx['ID']
            return redirect(url_for('home'))
        #---------------------------------------------------------------------    
        else:
            
            
            
            
            
            qry='insert into user_detail (Username,Password) values(%s,%s)'
            con.execute(qry,[username1,password1])
            mysql.connection.commit()
        #---------------------------------------------------------------------    
            
            syn=f'select*from user_detail where Username=%s and Password = %s'
            con.execute(syn,[username1,password1])
            result=con.fetchone()
        #---------------------------------------------------------------------    
            IDS_USER=result['ID']
            qry2=f"""
                    CREATE TABLE USER{IDS_USER} (
                ID INT PRIMARY KEY AUTO_INCREMENT,
                TITLE VARCHAR(50) NOT NULL,
                CONTENT VARCHAR(50) NOT NULL
                                                
                                            )
                """
            con.execute(qry2)
            mysql.connection.commit()
            con.close()
        #---------------------------------------------------------------------
            if result:
                
                XFACTOR = True
                RUN=0
                flash('New User Added')
                return redirect(url_for('home'))
        #---------------------------------------------------------------------
            else:
                
                return redirect(url_for('signin'))
    if XFACTOR==False or RUN==1:    #---------------------------------------------------------------------
        return render_template('none/signup.html')
    else:
        return redirect(url_for('home'))
    
    
#---------------------------------------------------------------------   
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html') 
  

#--------------------------------------------------------------------
@app.route('/')
def out():
    global XFACTOR
    if XFACTOR==False:
        
        return render_template('home.html')
        #---------------------------------------------------------------------
    else:
        return redirect(url_for('home'))
        #---------------------------------------------------------------------
#---------------------------------------------------------------------

@app.route('/logout')
def logout():
    global XFACTOR
    global RUN
    XFACTOR=False
    RUN=1
    return redirect(url_for('signin'))

    

    

#--------------------------------------------------------------------    
@app.route('/change',methods=['POST','GET'])
def change():
    global XFACTOR
    global RUN
    if request.method=='POST':
        usernameO = request.form['oldusername']
        passwordO = request.form['oldpassword']

        passwordN = request.form['newpassword']
        passwordC = request.form['conpassword']
        #---------------------------------------------------------------------
        con=mysql.connection.cursor()
        syn1231='select*from user_detail where Username=%s and Password = %s'
        xs=[usernameO,passwordO]
        con.execute(syn1231,xs)
        rest=con.fetchone()
        ids=rest['ID']
        if rest and passwordN == passwordC:
            con=mysql.connection.cursor()
            syn2="update user_detail set Password=%s where ID = %s "
            con.execute(syn2,[passwordN,ids])
            mysql.connection.commit()
            con.close()
            return redirect('signin')




    if XFACTOR==False or RUN==1:    #---------------------------------------------------------------------
        return render_template('none/FR.html')
    else:
        return redirect(url_for('home'))
#---------------------------------------------------------------------
if __name__=='__main__':

    app.run(host='0.0.0.0',port=5000,debug=True)

#---------------------------------------------------------------------
