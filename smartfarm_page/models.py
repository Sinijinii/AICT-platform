from django.db import models

# 앱에서 사용하는 데이터 구조를 정의하고 DB와의 소통을 담당하는 파일

from django.db import models


class FileUploadModel(models.Model):
    file = models.FileField(upload_to="")


class InputValueModel(models.Model):
    chojang = models.FloatField()


class All(models.Model):
    all_id = models.AutoField(primary_key=True)
    id = models.CharField(db_column='ID', max_length=5)  # Field name made lowercase.
    heartrate = models.IntegerField(db_column='HeartRate')  # Field name made lowercase.
    sc_field = models.IntegerField(db_column='sc_')  # Field renamed because it ended with '_'.
    error = models.CharField(max_length=12, blank=True, null=True)
    zsc = models.IntegerField(db_column='Zsc')  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    day = models.DateField(db_column='Day', blank=True, null=True)  # Field name made lowercase.
    time = models.TimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    week = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'all'
        unique_together = (('all_id', 'id'),)




class AllKids(models.Model):
    번호 = models.IntegerField()
    이름 = models.CharField(primary_key=True, max_length=5)
    생년월일 = models.DateField(blank=True, null=True)
    반 = models.CharField(max_length=12, blank=True, null=True)
    성별 = models.CharField(max_length=5, blank=True, null=True)
    성향 = models.CharField(max_length=5, blank=True, null=True)
    밴드_id = models.CharField(db_column='밴드_ID', max_length=25)  # Field name made lowercase.
    어린이집 = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'all_kids'
        unique_together = (('이름', '밴드_id'),)



