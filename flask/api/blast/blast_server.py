#coding:utf-8
import parser

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature
from flask_httpauth import HTTPTokenAuth
import json
from . import blast
from flask import request,jsonify
from api.model.login_model import User
from api import db

from .blastUtils import getHelp,test,byFastaAnalysis
from flask_restx import Api,Resource,reqparse
# 使用 http://127.0.0.1:5000/login 可查看所有的api
api = Api(blast, version="1.0", title="blast API", description="A simple blast API")
ns = api.namespace("blast-server", description="blast operations")
@ns.route('/blast')
class Blast(Resource):
    def get(self):
        getHelp()
        ss = """ATGAGCACCGAGATCGACTGGGCCGCCCTGCGCACCGCCGCGCGAGAGGCGATGGCGCACGCGTACGTGC
CGTACTCGACGTTCCCGGTGGGCGCGGCGGCGCTGGTCGACGACGGGCGGATCGTCAGCGGCTGCAATGT
GGAGAACGCTTCCTACGGGCTGACGCTGTGCGCCGAGTGCGGGCTGGTGTCCGCGCTGCACGCCTCCGGC
GGCGGGCGGCTGGTCGCCTTCGCCTGCGTCGACGGCGAAGGCGCGGCGCTGATGCCCTGCGGGCGGTGCC
GCCAGCTGCTGTTCGAGTTCGGGGGCACGGATCTGCTCGTGGATCTGGGCCCTGATTCGGAGCCGTCGGC
GACATCGCTGTCGGACCTCCTGCCCCGGGCCTTCGGTCCGGACAATCTCAGCAATCACAGCTAG"""
        s = byFastaAnalysis("blastn", "nt", ss)
        print(s)
        return 'blast'


@ns.route('/get-blast')
class getBlast(Resource):
    def post(self):
        parser = reqparse.RequestParser(trim=True)
        parser.add_argument('blast', location=['json', 'args'])
        data = parser.parse_args()
        print(json.loads(data['blast']))
        blastdata = json.loads(data['blast'])
        ret = byFastaAnalysis(blastdata['pro'], blastdata['db'], blastdata['sequence'])
        return ret

