#-*- coding: UTF-8 -*- 
from flask import Flask
from flask import session
from flask import redirect
from models import *
from hashmd5 import *
from check import check
from device import device
from data import data
from scene import scene
from rtc import rtc
from sendmsg import send_msg
from timing import timing

import os,stat


app=create_app()

##blueprint静态路由

app.register_blueprint(check)    #注册 登录
app.register_blueprint(device)   #获取设备信息
app.register_blueprint(data)  #获取设备历史信息
app.register_blueprint(scene)  #场景任务设置
app.register_blueprint(send_msg) #上传下载文件
app.register_blueprint(timing) #定时任务设置
app.register_blueprint(rtc) #实时任务设置
   
# 在测试时append(port)等信息 (debug=True)默认 在生产状态时一定不能开启 
if __name__=='__main__':
    app.run()