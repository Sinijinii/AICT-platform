from django.db import models

# str_smartfarm
class FileUploadModel(models.Model):
    file = models.FileField(upload_to="")

class InputValueModel(models.Model):
    chojang = models.FloatField()

from django.core.validators import RegexValidator

class PhoneNumberRegex(models.Model):
    phoneNumberRegex = RegexValidator(regex=r'?([0-9]{3,4})-?([0-9]{4})$')
    phone = models.CharField(validators=[phoneNumberRegex], max_length=8, unique=False)
    # unique=False 를 통해 동일한 전화번호로 중복해서 가입 가능


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        app_label = 'default'
        db_table = 'user'

    def __str__(self):
        return self.user_id

# kids pattern
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
    name = models.CharField(db_column='Name', max_length=5)
    class Meta:
        managed = False
        app_label = 'kids_db'
        db_table = 'all_d'
        unique_together = (('all_id', 'id', 'name'),)


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
        app_label = 'kids_db'
        db_table = 'all_kids'
        unique_together = (('이름', '밴드_id'),)