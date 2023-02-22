from django.db import models

# Create your models here.

class BookInfo(models.Model):
    # id 系统默认会生成
    name = models.CharField(max_length=10, unique=True)
    pub_date = models.DateField(null=True)  # 发布日期
    readcount = models.IntegerField(default=0)  # 阅读量
    commentcount = models.IntegerField(default=0)  # 评论量
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    # 修改表名 默认表名 子应用名_类名 都是小写
    class Meta:
        db_table = "bookinfo"
        verbose_name = "书籍管理"


class PeopleInfo(models.Model):
    # 定义一个有序字典
    GENDER_CHOICE = (
        (1, "male"),
        (2, "female")
    )

    name = models.CharField(max_length=10)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=1)
    description = models.CharField(max_length=30, null=True)
    is_delete = models.BooleanField(default=False)
    # 外键 系统会自动为外键添加 _id  # on_delete=models.CASCADE 如果对应的外键被删除，则该条记录也被删除
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = "peopleinfo"


