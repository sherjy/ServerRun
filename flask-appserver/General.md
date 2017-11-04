flask  以及flask-restful等扩展 

flask 轻量 可以token模仿长连接

部分注释已在代码内

curl 测试

只使用GET POST （DELETE、PUT等方法已不推荐

API添加

~~~
#flask依赖
from flask import Blueprint
from flask import request,jsonify,json 
蓝本路由管理

~~~

app.register_blueprint(check)    #注册 登录
app.register_blueprint(device)   #获取设备信息
app.register_blueprint(data)  #获取设备历史信息
app.register_blueprint(scene)  #场景任务设置
app.register_blueprint(send_msg) #上传下载文件
app.register_blueprint(timing) #定时任务设置
app.register_blueprint(rtc) #实时任务设置



web service接口优化

使用蓝本路由管理



注册登录

登录验证身份token

个人信息：

~~~
name = usersinfo.name;
qq = usersinfo.qq;
phone = usersinfo.phone;
wechat = usersinfo.wechat;
~~~



flask路由实现

~~~
if User.query.filter_by(username = username).first() is not None:
        abort(400) # existing user
    user = User(username = username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    
~~~



数据库依赖sqlalchemy

sqlite：/mysql：

~~~
sqlUrl="sqlite:////tmp/test.db"
~~~



访问设备数据

~~~
Data(id=id,startTime=startTime,endTime=endTime,amount=amount,device_id=device_id)
~~~

得到时间长度记录 用于训练



手机信息

~~~
			devicecode = device.id
			devicestate = device.state
            devicename =device.name
~~~



验证身份 hash散列存储

~~~
password_md5.hexdigest()
~~~



flask有几种验证方式 hash散列 sha1 sha256

散列最快 如果怕查库 可以加盐salt处理



rtc.py 只是设置实时任务

没有实时通讯功能 再考虑是否加入 以后做成socket 可以实现IM语音聊天

timing.py 定时任务

与设备数据记录关联 样本训练



设置场景 

在训练样本时的样本加入的场景 相当于标签



msg

图片 音频转发

在考虑一下采用何种实现

base64/IM邮箱直接复制/InputFileStream

json base64可以直接转 图片 音频在百兆级以下的生成都很方便

邮箱投递类似微信 消息转发 不过是实时聊天功能的

FileStream效果可能一般



