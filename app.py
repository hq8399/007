# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
import json
from conn import DbConn

app = Flask(__name__)


@app.route('/restful/api/<string:model_id>/<int:task_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_task(model_id, task_id):
    if request.method == 'GET':
        # return '获取:%s-%s' % (model_id, task_id)
        obj = {"total": 2, "rows": [{'firstname': "1", 'lastname': "567657657"}, {'firstname': "2", 'lastname': "二"}]};
        return obj
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


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/get/user', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_user():
    obj = {"total": 2, "rows": [{'firstname': "1", 'lastname': "一"}, {'firstname': "2", 'lastname': "二"}]};
    return obj


@app.route('/menu/tree', methods=['GET', 'POST', 'PUT', 'DELETE'])
def init_menu_tree():
    obj = [{
        "id": 1,
        "text": "Folder1",
        "iconCls": "icon-save",
        "children": [{
            "text": "File1",
            "checked": True
        }, {
            "text": "Books",
            "state": "open",
            "attributes": {
                "url": "/demo/book/abc",
                "price": 100
            },
            "children": [{
                "text": "PhotoShop",
                "checked": True
            }, {
                "id": 8,
                "text": "Sub Bookds",
                "state": "closed"
            }]
        }]
    }, {
        "text": "Languages",
        "state": "closed",
        "children": [{
            "text": "Java"
        }, {
            "text": "C#"
        }]
    }]
    json_obj = json.dumps(obj)
    return json_obj


if __name__ == '__main__':
    app.run()
