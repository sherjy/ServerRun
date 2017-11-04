# -*- coding: utf-8 -*-

from flask import Flask
from datetime import *
import random
from sqlalchemy import or_
from sqlalchemy import and_
from sqlalchemy import text
from flask.ext.script import Manager

from dbSetting import create_app,db,sqlUrl


fail=0
success=1
exception=2

if __name__ == '__main__':
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']=sqlUrl
    db.init_app(app)

    
#个人用户列表  主要包含 id username password phone等字段
class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(32),unique = True)
    password = db.Column(db.String(32))

    def add(self):
        try:
            tempUser=User.query.filter_by(username=self.username).first()
            if tempUser is None:
                db.session.add(self)
                db.session.commit()
                return success
            else:
                return fail
        except Exception, e:
            print e
            db.session.rollback()
            return exception
            
    def isExisted(self):
        tempUser=User.query.filter_by(username=self.username,password=self.password).first()
        if tempUser is None:
            return fail
        else:
            return success            
            
    def isExistedUsername(self):
        tempUser=User.query.filter_by(username=self.username).first()
        if tempUser is None:
            return fail
        else:
            return success
            
def getTokenInformation(username): 
    u=User.query.filter_by(username=username).first()
    return u



#个人用户列表  主要包含 id name phone qq wechat等字段
class UsersInfo(db.Model):
    __tablename__='usersinfos'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32))
    phone = db.Column(db.String(32))
    qq = db.Column(db.String(32))
    wechat = db.Column(db.String(32))
    token = db.Column(db.String(32))
    
    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception, e:
            print e 
            db.session.rollback()
            return exception
    
    
    

#硬件设备数据库列表  主要包含id user_id password type name等字段
class DeviceList(db.Model):
    __tablename__="devicelists"
    id = db.Column(db.Integer,primary_key=True)
    password = db.Column(db.String(32))
    type = db.Column(db.String(32))
    name = db.Column(db.String(32))
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    state = db.Column(db.String(32))
    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception, e:
            print e
            db.session.rollback()
            return exception
    
#历史数据列表  包含id，开启时间，停止时间，作用量，和设备id字段 
class HistoryData(db.Model):
    __tablename__="historydatas"
    id = db.Column(db.Integer,primary_key=True)
    starttime=db.Column(db.DateTime,default=datetime.now)
    endtime=db.Column(db.DateTime,default=datetime.now)
    amount=db.Column(db.Integer)
    device_id=db.Column(db.Integer,db.ForeignKey('devicelists.id'))
    
    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception, e:
            print e
            db.session.rollback()
            return exception 

#定时任务列表  包含id，任务编码和用户id    
class TimingTask(db.Model):
    __tablename__="timingtasks"
    id = db.Column(db.Integer,primary_key=True)
    deviceid = db.Column(db.Integer)
    starttime=db.Column(db.String)
    amount=db.Column(db.Integer) 
    days = db.Column(db.String)
    devicetype = db.Column(db.String)
    setflag = db.Column(db.String,default='0')
    userid = db.Column(db.Integer)
    sceneid = db.Column(db.Integer)


    
    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception, e:
            print e
            db.session.rollback()
            return exception

    def delete(self):
        tempTask=TimingTask.query.filter_by(deviceid=self.deviceid).first()
        try:
            db.session.delete(tempTask)
            db.session.commit()
        except Exception, e:
            print e
            db.session.rollback()
            return exception
       
            
#实时任务列表  包含id，任务编码和用户id              
class RealTimeTask(db.Model):
    __tablename__="realtimetasks"
    id = db.Column(db.Integer,primary_key=True)
    deviceid=db.Column(db.Integer)
    amount=db.Column(db.Integer) 
    devicetype = db.Column(db.String)
    setflag = db.Column(db.String,default='0')
    userid = db.Column(db.Integer)
    sceneid = db.Column(db.Integer)
    
    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception, e:
            print e
            db.session.rollback()
            return exception       
                                    
    def delete(self):
        tempTask=RealTimeTask.query.filter_by(deviceid=self.deviceid).first()
        try:
            db.session.delete(tempTask)
            db.session.commit()
        except Exception, e:
            print e
            db.session.rollback()
            return exception            
         

 #场景信息         
class Scene(db.Model):
    __tablename__ = 'scenes'
    id = db.Column(db.Integer,primary_key=True)
    taskcode = db.Column(db.String)
    user_id = db.Column(db.Integer)
    sceneid = db.Column(db.Integer)
    def add(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception, e:
            print e 
            db.session.rollback()
            return exception

    def delete(self):
        tempScene=Scene.query.filter_by(id=self.id,taskcode=self.taskcode).first();
        try:
            db.session.delete(tempScene)
            db.session.commit()
        except Exception, e:
            print e
            db.session.rollback()
            return exception            






