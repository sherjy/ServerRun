#-*- coding: UTF-8 -*- 
#正则匹配和hash散列
import hashlib
import re

def hashToken(username,password):
    password_md5=hashlib.md5()
    password_md5.update(username)
    password_md5.update(password)
    return password_md5.hexdigest()
    
def generatemd5(password):
    password_md5=hashlib.md5()
    password_md5.update(password)
    return password_md5.hexdigest()    



