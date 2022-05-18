from flask import Flask, render_template, request, jsonify
from day10.dao_emp import DaoEmp

app = Flask(__name__, static_url_path='')
# app = Flask(__name__)
de = DaoEmp()
@app.route('/emp')
def emp():
    return render_template("emp.html")

@app.route('/ajax')
def ajax():
    emps = de.myselects()
    return jsonify({'msg': '저장 완료!'}) 

@app.route('/ajax_list')
def ajax_list():
    list = de.myselects()
    return jsonify(list) 

@app.route('/ajax_one')
def ajax_one():
    e_id = request.args.get('e_id')
    one = de.myselect(e_id);
    return jsonify(one)

@app.route('/ajax_insert',methods=['POST'])
def ajax_insert():
    aa = request.get_json();
    e_id = aa['e_id']
    e_name = aa['e_name']
    sex = aa['sex']
    addr = aa['addr']
    cnt = de.myinsert(e_id, e_name, sex, addr)
    return jsonify(cnt)

@app.route('/ajax_update',methods=['POST'])
def ajax_update():
    aa = request.get_json();
    e_id = aa['e_id']
    e_name = aa['e_name']
    sex = aa['sex']
    addr = aa['addr']
    cnt = de.myupdate(e_id, e_name, sex, addr)
    return jsonify(cnt)

@app.route('/ajax_delete',methods=['POST'])
def ajax_delete():
    aa = request.get_json();
    e_id = aa['e_id']
    cnt = de.mydelete(e_id)
    return jsonify(cnt)

if __name__== "__main__":
    app.run(debug=True)