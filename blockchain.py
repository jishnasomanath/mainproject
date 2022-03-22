from flask import Flask,render_template,request
from DBConnection import Db
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def login():
    db=Db()
    if request.method=='POST':
        username=request.form['email']
        password=request.form['password']
        ss=db.selectOne("select * from login where username='"+username+"'and password='"+password+"'")
        if ss is not None:
            if ss['type']=='merchant':

    return render_template('login.html')

@app.route('/C_Registration',methods=['GET','POST'])
def C_Registration():
    db=Db()
    if request.method=='POST':
        cname=request.form['name']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        photo=request.form['photo']
    return render_template("customer/C_Registration.html")
@app.route('/M_Registration',methods=['GET','POST'])
def M_Registration():
    db=Db()
    if request.method=='POST':
        mname=request.form['m_name']
        mplace=request.form['m_place']
        mphone=request.form['m_phone']
        memail=request.form['memail']
        mphoto=request.form['mphoto']

    return render_template("merchant/M_Registration.html")
@app.route('/product_management',methods=['GET','POST'])
def product_management():
    db=Db()
    if request.method=='POST':
        productname=request.form['productname']
        bname=request.form['bname']
        price=request.form['price']
        des=request.form['description']
    return render_template("merchant/product_management.html")

if __name__ == '__main__':
    app.run()
