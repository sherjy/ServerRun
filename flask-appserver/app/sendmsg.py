#-*- coding: UTF-8 -*- 
# 打时间点 StartTime EndTime
from flask import Blueprint
from flask import request,jsonify,json 
from models import *

import traceback
import sys

send_msg=Blueprint("send_msg",__name__)

# 图片上传
@sendmsg.route('/picupload',methods=['POST'])
def picupload():
    try:
        token = request.json['token']
        src = request.json['picpath']
        dst = '//temp//'
        shutil.copyfile(src, dst)
        state = 'successful'
        reason = ''
    except Exception, e:
        print e
        state = 'fail'
        reason = ''
    return jsonify({'state':state,'reason':reason})

# 图片下载
@sendmsg.route('/picdownload',methods=['GET'])
def picdownload():
    try:
        token = request.json['token']
        src = request.json['picpath']
        dst = '//temp//'
        shutil.copyfile(src, dst)
        state = 'successful'
        reason = ''
    except Exception, e:
        print e
        state = 'fail'
        reason = ''
    return jsonify({'state':state,'reason':reason})

# 音频上传 append(base64/IM邮箱直接复制/InputFileStream)
@sendmsg.route('/musicupload',methods=['POST'])
def musicupload():
    try:
        token = request.json['token']
        src = request.json['picpath']
        dst = '//temp//'
        shutil.copyfile(src, dst)
        state = 'successful'
        reason = ''
    except Exception, e:
        print e
        state = 'fail'
        reason = ''
    return jsonify({'state':state,'reason':reason})

# 音频下载 append(base64/IM邮箱直接复制/InputFileStream)
@sendmsg.route('/musicdownload',methods=['GET'])
def musicdownload():
    try:
        token = request.json['token']
        src = request.json['picpath']
        dst = '//temp//'
        shutil.copyfile(src, dst)
        state = 'successful'
        reason = ''
    except Exception, e:
        print e
        state = 'fail'
        reason = ''
    return jsonify({'state':state,'reason':reason})
