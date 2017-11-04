#-*- coding: UTF-8 -*- 
# 定时任务操作
from flask import Blueprint
from flask import request,jsonify,json 
from models import *

import traceback
import sys

timing=Blueprint('timing',__name__)

# 设置定时任务 收集、训练样本 
@timing.route('/settimingtask',methods=["POST"])
def settimingtask():
    try:
        user_id=request.json['token']
        scenetask = request.json['scenetask']
        timingtask = TimingTask(user_id=user_id,taskcode=scenetask)
        timingtask.add()
        state = 'sucessful'
        reason = ''
    except Exception, e:
        print e 
        state = 'fail'
        reason = '服务器异常'
    return jsonify({'state':state,'reason':reason})        




@timing.route('/timingtask/add',methods=["POST"])
def add():
    try:
        id=request.values.get('id','default')
        taskcode=request.values.get('taskcode','default')
        user_id=request.values.get('user_id','default')
        
        tt=TimingTask(id=id,taskcode=taskcode,user_id=user_id)
        tt.add()
        state = 'successful'
        reason = ''
    except Exception, e:
        print e
        state = 'fail'
        reason = '服务器异常'
    return jsonify({'state':state,'reason':reason})

@timing.route('/timingtask/delete',methods=["POST"])
def delete():
    try:
        id=request.values.get('id','default')
        taskcode=request.values.get('taskcode','default')
        user_id=request.values.get('user_id','default')

        tempTask=TimingTask(id=id,taskcode=taskcode,user_id=user_id)
        try:
            tempTask.delete()
            state = 'successful'
            reason = ''
        except Exception, e:
            print e
            state = 'fail'
            reason = '数据库异常' 
    except Exception, e:
        print e
        state = 'fail'
        reason = '服务器异常'
               
    return jsonify({'state':state,'reason':reason})            
            
            
        



