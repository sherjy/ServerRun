#-*- coding: UTF-8 -*- 
# 关于设备的获取的功能，主要包括获取设备列表，获取设备具体状态等
from flask import Blueprint
from flask import request,jsonify,jsonify
from models import *
from hashmd5 import *

import traceback
import sys

device=Blueprint('device',__name__)

# 获取设备的列表
@device.route('/getdevicelist',methods=['POST'])
def getdevicelist():
    result = []
    try:
        token = request.json['token']
        devicelist = DeviceList.query.filter_by(user_id=token).all()
        if devicelist is None:
            state = 'fail'
            reason = '该设备不存在'
        else:    
            for device in devicelist:
                output={'deviceid':device.id,'type':device.type,'name':device.name}
                result.append(output)
            state = 'successful'
            reason = ''
        
    except Exception, e:
        print e 
        state = 'fail'
        reason = '服务器异常'
    return jsonify({'state':state,'reason':reason,'devicelist':result})

# 获取设备的某一状态
@device.route('/getdevicestate',methods=['POST'])
def getdevicestate():
    try:
        token = request.json['token']
        deviceid = request.json['deviceid']
        device = DeviceList.query.filter_by(user_id=token).filter_by(id=deviceid).first()
        if device is None:
            state = 'fail'
            reason = '该设备未使用'
            devicestate=''
        else:
            devicestate = device.state
            
            state = 'successful'
            reason = ''
    except Exception, e:
        print e 
        state = 'fail'
        reason = '服务器异常'            
        devicestate = ''
    return jsonify({'state':state,'reason':reason,'devicestate':devicestate})
    

# 获取某一设备历史数据
@device.route('/getdevicedata',methods=['POST'])
def getdevicedata():
    result=[]
    try:
        token = request.json['token']
        deviceid = request.json['deviceid']
        historydata = HistoryData.query.filter_by(device_id=deviceid).all()
        if historydata is None:
            state = 'fail'
            reason = '无历史数据'
        else:
            for data in historydata:
                output={'starttime':data.starttime,'amount':data.amount}
                result.append(output)
            state = 'successful'
            reason = ''
    except Exception, e:
        print e 
        state = 'fail'
        reason = '服务器异常'
    return jsonify({'state':state,'reason':reason,'historydata':result})        

# 获取某设备详细信息
@device.route('/getdevevicedetails',methods=['POST'])
def getdevicedetail():
    try:
        token = request.json['token']
        deviceid = request.json['deviceid']
        device = DeviceList.query.filter_by(user_id=token).filter_by(id=deviceid).first()
        if device is None:
            state = 'fail'
            reason = '该设备未使用'
            devicestate = ''
            devicename = ''
            devicecode = ''
        else:
            devicestate = device.state
            devicename =device.name
            devicecode = device.id
            state = 'successful'
            reason = ''
    except Exception, e:
        print e 
        state = 'fail'
        reason = '服务器异常'            
        devicestate = ''
    return jsonify({'state':state,'reason':reason,'devicestate':devicestate,'devicename':devicename,'devicecode':deviceid})    



#设备更新进数据库
@device.route('/devicelist/add',methods=['POST'])
def add():
    try:
        id=request.values.get('id','default')
        user_id='0'
        password='admin'
        type=request.values.get('type','default')
        name = id
        
        d=DeviceList.query.filter_by(id=str(id)).first()
        
        if d is None:
            d=DeviceList(id=id,password=password,type=type,name=name,user_id=user_id)
            d.add()
            state='successful'
            reason=''
        else:
            state = 'fail'
            reason = '设备已经注册'
            
    except Exception, e:
        print e
        state ='fail'
        reason='服务器异常'
    return jsonify({'state':state,'reason':reason})     

