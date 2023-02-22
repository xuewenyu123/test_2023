from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    return HttpResponse("ok")

##########新增数据#############
# 方式1
from book.models import BookInfo
book = BookInfo(
    name = "Django",
    pub_date = "2000-1-1",
    readcount = 10
)
book.save()
# 方式2  使用objects，作为代理，实现增删查改
BookInfo.objects.create(
    name = "测试开发入门",
    pub_date = "2020-1-1",
    readcount = 50
)

###########修改数据############
# 方式1
book = BookInfo.objects.get(id = 6)
book.name = "测试入门"
book.save()
# 方式2
BookInfo.objects.filter(id = 6).update(name = "爬虫入门", commentcount = 66)

############删除数据###############
# 方式1
book = BookInfo.objects.get(id = 6)
book.delete()
# 方式2
BookInfo.objects.get(id = 6).delete()
BookInfo.objects.filter(id = 6).delete()

###########查询结果##############
BookInfo.objects.all()

BookInfo.objects.all().count() # <=> 等价 BookInfo.objects.count()


############过滤查询###############
# 模型名.objects.filter(属性名__运算符=值)      # 查询N个结果 n = 0,1,2,3,。。。。
# 模型名.objects.exclude(属性名__运算符=值)     # 查询N个结果 n = 0,1,2,3,。。。   相当于notin
# 模型名.objects.get(属性名__运算符=值)         # 查询N个结果 n = 1 或 异常