from django.db import models


# 拠点
class Base(models.Model):
    # 拠点名（日本語）
    name_ja = models.CharField(max_length=100, unique=True, verbose_name='拠点名(日本語)')
    # 拠点名（英語）
    name_en = models.CharField(max_length=100, unique=True, verbose_name='拠点名(英語)')
    # 拠点コード
    no = models.IntegerField(primary_key=True, verbose_name='拠点コード')
    # 画像
    image = models.ImageField(upload_to='base_image', blank=True, verbose_name='画像')

    def __str__(self):
        return self.name_ja


# 食品
class Food(models.Model):
    # 品名
    name = models.CharField(max_length=100, verbose_name='品名')
    # カテゴリ
    category = models.CharField(max_length=100, verbose_name='カテゴリー')

    def __str__(self):
        return self.name


# 在庫
class Stock(models.Model):
    # 食品
    food = models.ForeignKey(Food, on_delete=models.CASCADE, verbose_name='品名')
    # 賞味期限
    date = models.DateField(blank=True, null=True, verbose_name='賞味期限')
    # 数量
    quantity = models.IntegerField(verbose_name='数量')
    # 拠点
    base = models.ForeignKey(Base, on_delete=models.SET_NULL, null=True, verbose_name='拠点')

    def __str__(self):
        return self.food.name


# スタッフ
class Staff(models.Model):
    # 名前
    name = models.CharField(max_length=100, verbose_name='名前')
    # 所属拠点
    base = models.ForeignKey(Base, on_delete=models.SET_NULL, null=True, verbose_name='所属拠点')

    def __str__(self):
        return self.name


# スタッフスケジュール
class StaffSchedule(models.Model):
    # スタッフの名前
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name='スタッフ名')
    # タスク
    task = models.CharField(max_length=100, verbose_name='タスク')
    # 開始日時
    start = models.DateTimeField(verbose_name='開始日時')
    # 終了日時
    end = models.DateTimeField(verbose_name='終了日時')

    def __str__(self):
        return self.staff.name


# 物流
class Distribution(models.Model):
    # 品名
    name = models.ManyToManyField(Stock, verbose_name='品名')
    #配送元
    ship_from = models.CharField(max_length=100, verbose_name='配送元')
    #配送先
    ship_to = models.CharField(max_length=100, verbose_name='配送先')
    # 品名
    name = models.CharField(max_length=100, verbose_name='品名')
    # 数量
    quantity = models.IntegerField(verbose_name='数量')
    #担当者
    staff = models.CharField(max_length=100, verbose_name='担当者')

    def __str__(self):
        return self.name
