#coding:utf-8
import parser

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature
from flask_httpauth import HTTPTokenAuth
import json
from . import login
from flask import request,jsonify
from api.model.login_model import User
from api import db
from flask_restx import Api,Resource,reqparse
# 使用 http://127.0.0.1:5000/login 可查看所有的api
api = Api(login, version="1.0", title="login API", description="A simple login API")
ns = api.namespace("login-server", description="logins operations")
SECRET_KEY = 'xiyang'
EXPIRED=15
# http://127.0.0.1:5000/login/login-server/test
@ns.route('/test')
class Servers(Resource):
   def get(self):
       print(verify_token("eyJhbGciOiJIUzUxMiIsImlhdCI6MTYyODQwNTU3MCwiZXhwIjoxNjI4NDA1NTg1fQ.eyJpZCI6IuWFtuWuniJ9.6Ks4jsDHVEVfH2Bg1u4BMX5QMqZKCVN2-W402wBkTsDdWI1jGmDKawXYewi_FINzYskAig_Tz3YU3WsnMHKf4A"))
       return 'this is data list'

parser = reqparse.RequestParser(trim=True)
parser.add_argument('users', location=['json', 'args'])

@ns.route('/users')
class Users(Resource):
    def get(self):
        data = parser.parse_args()
        # print(json.loads(data['users']))
        userdata = json.loads(data['users'])
        user = User.query.filter_by(name=userdata['name'], password=userdata['password']).first()
        s = Serializer(SECRET_KEY, expires_in=EXPIRED)
        # token
        token = s.dumps({"id": userdata['name']}).decode('ascii')
        print(token)
        if user == None:
            return jsonify({"message":"没有查询到该用户", "code": 400})
        else:
            return jsonify({"message": "success", "code": 200, "token":token})

    def post(self):
        data = parser.parse_args()
        # print(json.loads(data['users']))
        userdata = json.loads(data['users'])
        user = User.query.filter_by(name=userdata['name'], password=userdata['password']).first()
        if user == None:
            # 写入数据库
            user = User(name=userdata['name'], password=userdata['password'])
            db.session.add(user)
            db.session.commit()
            print(user.id)
            # token
            s = Serializer(SECRET_KEY, expires_in=EXPIRED)
            token = s.dumps({"id": userdata['name']}).decode('ascii')
            return jsonify({"message":'注册成功',"code":200, "data":{"id":user.id,"token":token}})
        else:
            return jsonify({"message": '用户已存在', "code": 400, "data": user.id})


auth = HTTPTokenAuth(scheme='JWT')
@auth.verify_token
def verify_token(token):
    # SECRET_KEY:内部的私钥，这里写在配置信息里
    s = Serializer(SECRET_KEY)
    try:
        data = s.loads(token)
        print("token",data)
    except BadSignature:
        print('token不正确')
    except SignatureExpired:
        print('token过期')
    # 校验通过返回True
    return True