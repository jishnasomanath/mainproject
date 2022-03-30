from flask import Flask,render_template,request,session,redirect
from DBConnection import Db
import datetime
app = Flask(__name__)
app.secret_key="abc"


@app.route('/',methods=['GET','POST'])
def login():
    db=Db()
    if request.method=='POST':
        username=request.form['email']
        password=request.form['password']
        ss=db.selectOne("select * from login where username='"+username+"'and password='"+password+"'")
        if ss is not None:
            if ss['type']=='merchant':
                session['mid']=ss['loginid']
                return redirect('/merchant_home')
            elif ss['type']=='customer':
                session['cid']=ss['loginid']
                return redirect('/customer_home')
            else:
                return '<script>alert("invalid username or password");window.location="/"</script>'
        else:
            return '<script>alert("user not exist");window.location="/"</script>'

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
        pname=request.form['productname']
        bname=request.form['bname']
        location=request.form['location']
        ingredients=request.form['ingredients']
        price=request.form['price']
        des=request.form['usagedetails']
        photo=request.files['photo']
        date=datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        photo.save(r"C:\Users\VISHNU\PycharmProjects\blockchain\static\product\\"+date+'.jpg')
        photo1="/static/product/"+date+'.jpg'
        db.insert("insert into product_management(p_name,p_location,Brand_name,ingredients,price,description,p_photo) values('"+pname+"','"+location+"','"+bname+"','"+ingredients+"','"+price+"','"+des+"','"+photo1+"') ")
        return "ok"
    return render_template("merchant/product_management.html")
@app.route('/view_product')
def view_product():
    db=Db()
    ss=db.select("select * from product_management ")
    return render_template("merchant/view_product.html",data=ss)
@app.route('/delete_product/<p>')
def delete_product(p):
    db=Db()
    ss=db.delete("delete  from product_management where pid='"+str(p)+"'")
    return redirect('/view_product')
@app.route('/update_product/<p>',methods=['GET','POST'])
def update_product(p):
    db=Db()
    if request.method=='POST':
        pname=request.form['productname']
        bname=request.form['bname']
        location=request.form['location']
        ingredients=request.form['ingredients']
        price=request.form['price']
        desc=request.form['description']
        photo=request.files['photo']
        date=datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        photo.save(r"C:\Users\VISHNU\PycharmProjects\blockchain\static\product\\"+date+'.jpg')
        photo1="/static/product/"+date+'.jpg'
        if request.files!=None:
            if photo.filename!="":
                db.update(" update  product_management set p_name='"+pname+"',p_location='"+location+"',Brand_name='"+bname+"',ingredients='"+ingredients+"',price='"+price+"',description='"+desc+"',p_photo='"+photo1+"' where pid='"+p+"'")
                return "ok"
            else:
                db.update(
                    " update  product_management set p_name='" + pname + "',p_location='" + location + "',Brand_name='" + bname + "',ingredients='" + ingredients + "',price='" + price + "',description='" + desc +"' where pid='"+p+"' ")
                return "ok"
        else:
            db.update(
                " update  product_management set p_name='" + pname + "',p_location='" + location + "',Brand_name='" + bname + "',ingredients='" + ingredients + "',price='" + price + "',description='" + desc + "' where pid='"+p+"' ")
            return "ok"
    else:
        ss=db.selectOne("select * from product_management where pid='"+p+"'")
        return render_template("merchant/update_product.html",data=ss)
@app.route('/merchant_home',methods=['GET','POST'])
def merchant_home():
    db=Db()
    return render_template("merchant/merchant_home.html")
@app.route('/customer_home',methods=['GET','POST'])
def customer_home():
    db=Db()
    return render_template("customer/customer_home.html")

if __name__ == '__main__':
    app.run()
