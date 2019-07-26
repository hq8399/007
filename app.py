# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
from conn import DbConn

app = Flask(__name__)


@app.route('/restful/api/<string:model_id>/<int:task_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_task(model_id, task_id):
    if request.method == 'GET':
        return '获取:%s-%s' % (model_id, task_id)
    if request.method == 'POST':
        data = request.data
        sql = "select * from res_partner"
        res_partner = DbConn(sql).pgConn()
        return '创建:%s-%s-%s' % (model_id, task_id, res_partner)
    if request.method == 'PUT':
        data = request.data
        return '更新:%s-%s-%s' % (model_id, task_id, data)
    if request.method == 'DELETE':
        return '删除:%s-%s' % (model_id, task_id)


@app.route('/user')
def user():
    return render_template('user.html')


@app.route('/get/user', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_user():
    obj = {"total": 2, "rows": [{'firstname': "1", 'lastname': "一"}, {'firstname': "2", 'lastname': "二"}]};
    return obj


if __name__ == '__main__':
    app.run()
