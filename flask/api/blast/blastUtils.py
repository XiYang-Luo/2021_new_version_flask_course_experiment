# -*- coding: utf-8 -*-
'''document BioPython   https://biopython-cn.readthedocs.io/zh_CN/latest/cn/chr07.html'''
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO
from flask import jsonify


def __init__():
    pass

def getHelp():
    help(NCBIWWW.qblast)

def test():
    return {"code": 1, "data": {"E_VALUE_THRESH": 0.04, "content": [[{"seq": "SEQ", "hsp-query": "ATTCGTTGCAAAG",
                                                                          "hsp-match": "|||||||||||||", "e-value": 0.11,
                                                                          "hsp-sbjct": "AAAACCTGCAG", "lenght": 29}]]}}

def byFastaAnalysis(pro, db, seq):
    print("en")
    E_VALUE_THRESH = 0.04  # 打印出所有大于某一特定阈值的BLAST命中结果的一些汇总信息
    # record = SeqIO.read(r"C:\Users\Luo XiYang\Desktop\sequence.fasta", format="fasta")
    # result_handle2 = NCBIWWW.qblast("blastn", "nt", record.seq)
    result_handle2 = NCBIWWW.qblast(pro, db, seq)
    blast_record = NCBIXML.read(result_handle2)
    if blast_record is None:
        return {"code": 400, "data": {}}
    else:
        content = [];
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                if hsp.expect < E_VALUE_THRESH:
                    '''
                        print('sequence:', alignment.title)
                        print( 'length:', alignment.length)
                        print( 'e value:', hsp.expect)
                        print( hsp.query[0:75] + '...')
                        print( hsp.match[0:75] + '...')
                        print( hsp.sbjct[0:75] + '...')
                        print("\n\n\n")
                    '''
                    content.append([{"seq": alignment.title, "e-value": hsp.expect,
                                         "hsp-query": hsp.query[0:] + '...', "hsp-match": hsp.match[0:] + '...', \
                                         "hsp-sbjct": hsp.sbjct[0:] + '...', "lenght": alignment.length}])
        print(blast_record.query)
        return {"code": 200, "data": {"E_VALUE_THRESH": 0.04, "content": content}}

    '''读取本地文档进行解析'''

def readXML():
    E_VALUE_THRESH = 0.04
    result_handle = open(r"C:\Users\Luo XiYang\Desktop\sequence.xml")
    blast_record = NCBIXML.read(result_handle)
    blast_records = NCBIXML.parse(result_handle)
    print(blast_record)
    content = [];
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < E_VALUE_THRESH:
                print('sequence:', alignment.title)
                print('length:', alignment.length)
                print('e value:', hsp.expect)
                print(hsp.query[0:] + '...')
                print(hsp.match[0:] + '...')
                print(hsp.sbjct[0:] + '...')
                print("\n\n\n")
                content.append([{"seq": alignment.title, "e-value": hsp.expect, "hsp-query": hsp.query[0:] + '...',
                                     "hsp-match": hsp.match[0:] + '...', \
                                     "hsp-sbjct": hsp.sbjct[0:] + '...', "lenght": alignment.length}])
    return jsonify({"E_VALUE_THRESH": 0.04, "content": content})
