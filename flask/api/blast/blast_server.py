#coding:utf-8
import parser

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature
from flask_httpauth import HTTPTokenAuth
import json
from . import blast
from flask import request,jsonify
from api.model.login_model import User,BlastModel
from api import db

from .blastUtils import getHelp,test,byFastaAnalysis
from flask_restx import Api,Resource,reqparse
# 使用 http://127.0.0.1:5000/blast 可查看所有的api
from ..login.login_server import verify_token

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
        vt = verify_token(blastdata['token'])
        if vt['code'] == 400:
            return jsonify({"message":"token验证失败","code":500})
        vt_data = vt["data"]
        print(vt_data)
        ret = byFastaAnalysis(blastdata['pro'], blastdata['db'], blastdata['sequence'])
        # ret = {"code": 200, "data": {"E_VALUE_THRESH": 0.04, "content": [[{"seq": "SEQ", "hsp-query": "ATTCGTTGCAAAG",
        #                                                                   "hsp-match": "|||||||||||||", "e-value": 0.11,
        #                                                                   "hsp-sbjct": "AAAACCTGCAG", "lenght": 29}]]}}
        retdata = ret['data']
        e_value = '0.04'
        content = []
        content_seq,content_hsp_match,content_hsp_query,content_hsp_sbjct,content_e_value,content_lenght = '','','','','',''

        if ret['code'] == 200:
            e_value = retdata['E_VALUE_THRESH']
            content = retdata['content'][0][0]
            content_seq = content['seq']
            content_hsp_match = content['hsp-match']
            content_hsp_query = content['hsp-query']
            content_hsp_sbjct = content['hsp-sbjct']
            content_e_value = content['e-value']
            content_lenght = content['lenght']
        else:
            pass
        blastModel = BlastModel(
            user_id=int(vt_data['id']),
            user_name=vt_data['name'],
            project_name=blastdata['pro'],
            db_ncbi=blastdata['db'],
            sequence=blastdata['sequence'],
            e_value=e_value,
            content_seq = str(content_seq),
            content_hsp_match=str(content_hsp_match),
            content_hsp_query=str(content_hsp_query),
            content_hsp_sbjct=str(content_hsp_sbjct),
            content_e_value=str(content_e_value),
            content_lenght=str(content_lenght)
        )
        db.session.add(blastModel)
        db.session.commit()
        print(blastModel.id)
        return {"message":"success","code":200}

@ns.route('/get-blast-history')
class getBlastHistory(Resource):
    def get(self):
        parser = reqparse.RequestParser(trim=True)
        parser.add_argument('blast_history', location=['json', 'args'])
        data = parser.parse_args()
        print("93",json.loads(data['blast_history']))
        blastHistoryData = json.loads(data['blast_history'])
        vt = verify_token(blastHistoryData['token'])
        if vt['code'] == 400:
            return jsonify({"message": "token验证失败", "code": 500})
        vt_data = vt["data"]
        name = vt_data['name']
        user_id = int(vt_data['id'])
        print(name,user_id)
        blastHistory = BlastModel.query.filter_by(user_id=user_id,user_name=name).all()
        print(blastHistory)
        if len(blastHistory)>=1:
            ret_data = []
            for row in blastHistory:
                ret_data.append({"id": row.id, "seq": row.sequence,"user_name": row.user_name,
                                "user_id": row.user_id,"project_name":row.project_name,
                                 "db_ncbi": row.db_ncbi,"e_value": row.e_value,"create_time": row.create_time,
                                 "content_seq": row.content_seq, "content_hsp_match": row.content_hsp_match,
                                 "content_hsp_query": row.content_hsp_query, "content_hsp_sbjct": row.content_hsp_sbjct,
                                 "content_e_value": row.content_e_value, "content_lenght": row.content_lenght})
            response = jsonify({"code": 200, "message": "success", "data": ret_data})
            return response
        else:
            return jsonify({"message": "没有数据", "code": 400})

