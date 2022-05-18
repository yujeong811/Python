from flask import Flask
from flask.templating import render_template
from day10 import dao_emp
from day10.dao_emp import DaoEmp
from flask.globals import request
 
app = Flask(__name__)
de = DaoEmp()
@app.route('/list')
def list():
    emps = de.myselects()
    return render_template("list.html",emps=emps)

@app.route('/add')
def add():
    return render_template("add.html")

@app.route('/add_act', methods=['POST'])
def add_act():
    e_id = request.form.get('e_id')
    e_name = request.form.get('e_name')
    sex = request.form.get('sex')
    addr = request.form.get('addr')    
    cnt = de.myinsert(e_id, e_name, sex, addr)
    
    return render_template("add_act.html", cnt=cnt)

@app.route('/modify')
def modify():
    e_id = request.args.get('e_id')
    emp = de.myselect(e_id)
    
    return render_template("modify.html",emp=emp)

@app.route('/mod_act', methods=['POST'])
def mod_act():
    e_id = request.form.get('e_id')
    e_name = request.form.get('e_name')
    sex = request.form.get('sex')
    addr = request.form.get('addr')    
    cnt = de.myupdate(e_id, e_name, sex, addr)
    
    return render_template("mod_act.html", cnt=cnt)

@app.route('/del_act')
def del_act():
    e_id = request.args.get('e_id')  
    cnt = de.mydelete(e_id)
    
    return render_template("del_act.html", cnt=cnt)
 
if __name__== "__main__":
    app.run(debug=True)