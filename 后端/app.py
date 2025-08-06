import time
import flask
import random
import os
import SQLHandler
from flask_cors import CORS
from werkzeug.utils import secure_filename

db_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'root',
    'charset': 'utf8',
    'db': 'zhengning_db'
}
FILE_DIRE = 'File'

app = flask.Flask(__name__)
# 启用CORS，允许前端跨域请求
CORS(app, resources={r'/*': {'origins': '*'}})
sqlhandler = SQLHandler.SQLHandler(db_config)
func_dict = {
    'i_problem_orientation': sqlhandler.i_problem_orientation,
    'i_principle_exploration': sqlhandler.i_principle_exploration,
    'i_engineering_practice': sqlhandler.i_engineering_practice,
    'i_product_display': sqlhandler.i_product_display,
    'get_problem_orientation': sqlhandler.get_problem_orientation,
    'get_principle_exploration': sqlhandler.get_principle_exploration,
    'get_engineering_practice': sqlhandler.get_engineering_practice,
    'get_product_display': sqlhandler.get_product_display
}

def use_handle(method_addr, requests_json=None):
    try:
        if requests_json:
            result = func_dict[method_addr](**requests_json)
        else:
            result = func_dict[method_addr]()
        
        if method_addr.startswith('i_'):
            return flask.jsonify({'code': 200, 'msg': 'insert OK'})
        else:
            return flask.jsonify({'code': 200, 'data': result})
    except Exception as e:
        return flask.jsonify({'code': 500, 'msg': f'operation error: {e}'})

# 问题定向
@app.route('/problem-orientation', methods=['POST'])
def problem_orientation():
    return use_handle('i_problem_orientation', flask.request.json)

@app.route('/problem-orientation/list', methods=['GET'])
def problem_orientation_list():
    return use_handle('get_problem_orientation')

@app.route('/problem-orientation/<int:id>', methods=['GET'])
def problem_orientation_detail(id):
    return use_handle('get_problem_orientation')

# 原理探究
@app.route('/Principle-exploration', methods=['POST'])
def principle_exploration():
    return use_handle('i_principle_exploration', flask.request.json)

@app.route('/Principle-exploration/list', methods=['GET'])
def principle_exploration_list():
    return use_handle('get_principle_exploration')

@app.route('/Principle-exploration/<int:id>', methods=['GET'])
def principle_exploration_detail(id):
    return use_handle('get_principle_exploration')

# 工程实践
@app.route('/engineering-practice', methods=['POST'])
def engineering_practice():
    return use_handle('i_engineering_practice', flask.request.json)

@app.route('/engineering-practice/list', methods=['GET'])
def engineering_practice_list():
    return use_handle('get_engineering_practice')

@app.route('/engineering-practice/<int:id>', methods=['GET'])
def engineering_practice_detail(id):
    return use_handle('get_engineering_practice')

# 产品展示
@app.route('/Product-Display', methods=['GET', 'POST'])
def product_display():
    if flask.request.method == 'GET':
        if flask.request.args.get('tip') == '1':
            return flask.render_template('display.html')
        return flask.jsonify({'code': 400, 'msg': 'Invalid request'})
    
    c = flask.request.files['c']
    d = flask.request.files['d']
    print(c, d)
    if not c and d:
        return flask.jsonify({'code': 400, 'msg': 'No files uploaded'})
    
    c_filename = secure_filename(c.filename)
    d_filename = secure_filename(d.filename)
    
    os.makedirs(FILE_DIRE, exist_ok=True)
    
    cpath = f'{FILE_DIRE}/{int(time.time() * 10000)}-{random.randint(10000, 99999)}-{c_filename}'
    dpath = f'{FILE_DIRE}/{int(time.time() * 10000)}-{random.randint(10000, 99999)}-{d_filename}'
    c.save(f'{cpath}')
    d.save(f'{dpath}')
    my_json = {
        'a': flask.request.form.get('a'),
        'b': flask.request.form.get('b'),
        'c': cpath,
        'd': dpath
    }
    print(my_json)
    return use_handle('i_product_display', my_json)

@app.route('/Product-Display/list', methods=['GET'])
def product_display_list():
    return use_handle('get_product_display')

@app.route('/Product-Display/<int:id>', methods=['GET'])
def product_display_detail(id):
    return use_handle('get_product_display')

# 文件访问接口
@app.route('/file', methods=['GET'])
def get_file():
    file_path = flask.request.args.get('path')
    if not file_path or '..' in file_path:
        return flask.jsonify({'code': 400, 'msg': 'Invalid file path'})
    
    try:
        return flask.send_file(file_path)
    except Exception as e:
        return flask.jsonify({'code': 404, 'msg': f'File not found: {e}'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)