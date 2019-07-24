# -*- coding: utf-8 -*-

from flask import Flask, request
from conn import DbConn

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


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


if __name__ == '__main__':
    app.run()
