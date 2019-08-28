from django.db import models


# 拠点
class Base(models.Model):
    # 拠点名（日本語）
    name_ja = models.CharField(max_length=100, unique=True)
    # 拠点名（英語）
    name_en = models.CharField(max_length=100, unique=True)
    # 拠点コード
    no = models.IntegerField(primary_key=True)
    # 画像
    image = models.ImageField(upload_to='base_image', blank=True)

    def __str__(self):
        return self.name_ja


# 食品
class Food(models.Model):
    # 品名
    name = models.CharField(max_length=100)
    # カテゴリ
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 在庫
class Stock(models.Model):
    # 食品
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    # 賞味期限
    date = models.DateField(blank=True, null=True)
    # 数量
    quantity = models.IntegerField()
    # 拠点
    base = models.ForeignKey(Base, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.food__name


# スタッフ
class Staff(models.Model):
    # 名前
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 物流
class Distribution(models.Model):
    # 品名
    name = models.ManyToManyField(Stock)
    #配送元
    ship_from = models.CharField(max_length=100)
    #配送先
    ship_to = models.CharField(max_length=100)
    # 品名
    name = models.CharField(max_length=100)
    # 数量
    quantity = models.IntegerField()
    #担当者
    staff = models.CharField(max_length=100)

    def __str__(self):
        return self.name
