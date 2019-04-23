from django.db import models

# 在庫管理
class Stock(models.Model):
    # 品名
    name = models.CharField(max_length=100)
    # カテゴリ
    category = models.CharField(max_length=100)
    # 賞味期限
    date = models.DateField(blank=True, null=True)
    # 数量
    quantity = models.IntegerField()

    def __str__(self):
        return self.name