#-*- coding: UTF-8 -*- 

from flask import Blueprint
from flask import request,jsonify,json
from models import *

import traceback
import sys

data=Blueprint('data',__name__)


#增添一条设备历史数据
@data.route('/data/add',methods=["POST"])
def adddata():
    try:
        id=request.values.get('id','default')
        startTime=request.values.get('startTime','default')
        endTime=request.values.get('endTime','default')
        amount=request.values.get('amount','default')
        device_id=request.values.get('device_id','default')
        
        h=HistoryData(id=id,startTime=startTime,endTime=endTime,amount=amount,device_id=device_id)
        h.add()
        state='successful'
        reason = ''
    except Exception, e:
        print e
        state = 'fail'
        reason = '服务器异常'
    return  jsonify({'state':state,'reason':reason})
        




