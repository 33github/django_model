# _*_ coding:utf-8 _*_
from django.shortcuts import render
import pymysql
pymysql.install_as_MySQLdb()
# Create your views here.

from .models import UserMessage

def getform(request):
    #1.数据库查询
    # all_message = UserMessage.objects.all()   #默认的数据表管理器objects,all()将数据库所有的记录返回给值
    # name_message = UserMessage.objects.filter(name="bobby",address="北京")   #取数据库中name为bobby，address为北京
    # #all_message 这个值是django的内置类型，支持for循环
    # for message in all_message:
    #     print(message.name)

    # #完成数据表的传输，会根据setting中已配置好的数据库连接数据库
    # user_message = UserMessage()
    # user_message.name = "boddy2"
    # user_message.message = "helloworld2"
    # user_message.address = "上海"
    # user_message.email = "2@2.com"
    # user_message.object_id = "helloworld2"
    # user_message.save()

    #2.数据库增加，表单提交的东西加入到数据库
    # if request.method == "POST":
    #     #取出用户提交的值，注意要和message_form.html中input标签的id对应
    #     name = request.POST.get("name","")
    #     message = request.POST.get("message","")
    #     address = request.POST.get("address","")
    #     email = request.POST.get("email","")
    #     #取出来的值赋给model
    #     user_message = UserMessage()
    #     user_message.name = name
    #     user_message.message = message
    #     user_message.address = address
    #     user_message.email = email
    #     user_message.object_id = "helloworld3"
    #     user_message.save()

    #3.删除数据库中的数据
    name_message = UserMessage.objects.filter(name="bobby", address="北京")  # 取数据库中name为bobby，address为北京
    # name_message.delete()   #删除所有数据
    for message in name_message:
        message.delete()   #调用models中的方法delete()
        # print(message.name)

    return render(request,'message_form.html')

#为了说明models好用
# def book_list(request):
#     db = pymysql.connect(user = "me", db = "mydb", passwd = "secret", host = "localhost")   #连接数据库
#     cursor = db.cursor()   #创建执行器
#     cursor.execute("SLECT name FROM books ORDER BY name")   #执行原生SQL语句
#     names = [row[0] for row in cursor.fetchall()]   #将它遍历回来的数据当成一个数组去取某一个
#     db.close()

