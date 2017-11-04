#-*- coding: UTF-8 -*- 
#训练场景
import os
import traceback
import sys
import string
import shutil
import uuid


from flask import Blueprint
from flask import request,jsonify,json
from models import *



scene=Blueprint("scene",__name__)

UPLOAD_FOLDER = ''



# 设置设备场景任务
@scenetask.route('/setscenetask',methods=['POST'])
def setscenetask():
    try:
        id = request.json['token']
        scenetask = request,json['scenetask']
        scene = Scene(user_id=id,taskcode=scenetask)
        scene.add();
        state = 'successful'
        reason = ''
    except Exception, e:
        print e
        state = 'fail'
        reason = '服务器异常'
    return jsonify({'state':state,'reason':reason})

# 获取个人场景列表
@scenetask.route('/getscenetask',methods=['POST'])
def getscenetask():
    result = []
    try:
        id =request.json['token']
        scenelist = Scene.query.filter_by(user_id=id).all()
        if scenelist is None:
            state = 'fail'
            reason = '该用户之前未创建场景'
        else:
            for scene in scenelist:
                output = {'scenetask':scene.taskcode}
                result.append(output)
            state = 'successful'
            reason = ''
    except Exception, e:
        print e 
        state = 'fail'
        reason = '服务器异常'
    return jsonify({'state':state,'reason':reason,'scenelist':result})                   


# 增加个人场景
@scenetask.route('/addscenetask',methods=['POST'])
def addscenetask():
    try:
        token = request.json['token']
        sceneid = request.json['sceneid']
        scenelist = request.json['scenelist']
        json_string=json.dumps(scenelist)
        scenedata=json.loads(json_string)
        for scenechange in scenedata:
            temp=Scene(user_id=token,taskcode=scenechange['scenetask'],sceneid=sceneid)
            temp.add()
            tempdata=json.loads(scenechange['scenetask'])
            if tempdata['tasktype'] == '0':             #定时任务 更新进对应的表中
                try:
                    deviceid=tempdata['deviceid']
                    starttime = tempdata['starttime']
                    days = tempdata['days']
                    devicetype = tempdata ['devicetype']
                    amount = tempdata ['amount']
                    temptimingtask=TimingTask(deviceid=deviceid,starttime=starttime,days=days,devicetype=devicetype,amount=amount,userid=token,sceneid=sceneid)
                    temptimingtask.add()
                    state = 'successful'
                    reason = ''     
                except Exception, e:
                    print e 
                    state = 'fail'
                    reason = '通讯协议字段不完整'    
            else:                                       #实时任务 更新进对应的表中
                try:
                    deviceid=tempdata['deviceid']
                    devicetype = tempdata ['devicetype']
                    amount = tempdata ['amount']
                    realtimetask=RealTimeTask(deviceid=deviceid,amount=amount,devicetype=devicetype,userid=token,sceneid=sceneid)
                    realtimetask.add()
                    state = 'successful'
                    reason = ''     
                except Exception, e:
                    print e 
                    state = 'fail'
                    reason = '通讯协议字段不完整'  

    except Exception, e:
        print e 
        state = 'fail'
        reason = '服务器异常'    
    return jsonify({'state':state,'reason':reason})                   
        
# 修改个人场景
@scenetask.route('/editscenetask',methods=['POST'])
def editscenetask():
    try:
        token = request.json['token']
        sceneid = request.json['sceneid']
        scenelist = request.json['scenelist']
        
        json_string=json.dumps(scenelist)
        scenedata=json.loads(json_string)
        for scenechange in scenedata:
            temp=Scene(user_id=token,taskcode=scenechange['scenetask'],sceneid=sceneid)
            temp.add()
            tempdata=json.loads(scenechange['scenetask'])
            if tempdata['tasktype'] == '0':             #定时任务 更新进对应的表中
                try:
                    deviceid=tempdata['deviceid']
                    starttime = tempdata['starttime']
                    days = tempdata['days']
                    devicetype = tempdata ['devicetype']
                    amount = tempdata ['amount']
                    temptimingtask=TimingTask.query.filter_by(deviceid=deviceid,userid=token,sceneid=sceneid).first()
                    if temptimingtask is not None:                    
                        try:
                            temptimingtask.setflag='3';
                            db.session.add(temptimingtask)
                            db.session.commit()
                            temptask = TimingTask(deviceid=deviceid,starttime=starttime,days=days,devicetype=devicetype,amount=amount,userid=token,sceneid=sceneid)
                            temptask.add()
                            state = 'successful'
                            reason = ''     
                        except Exception, e:
                            db.session.rollback()
                            print e 
                            state ='fail'
                            reason = '数据库无法提交更改'                        
                    else:
                        state = 'fail'
                        reason ='该场景未设置'
                        
                except Exception, e:
                    print e 
                    state = 'fail'
                    reason = '通讯协议字段不完整'    
            else:                                       #实时任务 更新进对应的表中
                try:
                    deviceid=tempdata['deviceid']
                    devicetype = tempdata ['devicetype']
                    amount = tempdata ['amount']
                    realtimetask=RealTimeTask.query.filter_by(deviceid=deviceid,userid=token,sceneid=sceneid).first()
                    if realtimetask is not None:                       
                        try:
                            realtimetask.setflag = '3'                   
                            db.session.add(realtimetask)
                            db.session.commit()
                            realtimetask=RealTimeTask(deviceid=deviceid,amount=amount,devicetype=devicetype,userid=token,sceneid=sceneid)
                            realtimetask.add()
                            state = 'successful'
                            reason = ''                             
                        except Exception, e:
                            db.session.rollback()
                            print editscenelist
                            state = 'fail'
                            reason = '数据库无法提交'    
                    else:
                        state = 'fail'
                        reason ='该场景未设置'
                except Exception, e:
                    print e 
                    state = 'fail'
                    reason = '通讯协议字段不完整'          
    except Exception, e:
        print e 
        state = 'fail'
        reason = '服务器异常'    
    return jsonify({'state':state,'reason':reason})           

# 删除任务 
@scenetask.route('/delescenetask',methods=['POST'])
def delescenetask():
    try:
        token = request.json['token']
        sceneid = request.json['sceneid']
        tempreal=RealTimeTask.query.filter_by(userid=token,sceneid=sceneid).all()   
        if tempreal is not None: 
            for temptask in tempreal:
                try:
                    temptask.setflag = '3'
                    db.session.add(temptask)
                    db.session.commit()
                except Exception, e:
                    db.session.rollback()
                    state ='fail'
                    reason ='数据库无法提交更改'
        else:
            print None 
        temptiming =TimingTask.query.filter_by(userid=token,sceneid=sceneid).all()
        if temptiming is not None:
            for temptask in temptiming:
                try:
                    temptask.setflag = '3'
                    db.session.add(temptask)
                    db.session.commit()
                except Exception, e:
                    db.session.rollback()
                    state ='fail'
                    reason ='数据库无法提交更改'
        else:
            print None
        state = 'successful'
        reason =''
    except Exception, e:
        print e 
        state ='fail'
        reason ='服务器异常'    
    return jsonify({'state':state,'reason':reason})  
      

