from django.db import models

# 앱에서 사용하는 데이터 구조를 정의하고 DB와의 소통을 담당하는 파일

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
        db_table = 'user'

    def __str__(self):
        return self.user_id

class Environment(models.Model):
    user_num = models.OneToOneField('User', models.DO_NOTHING, db_column='user_num', primary_key=True)
    farm_id = models.CharField(max_length=45)
    date = models.DateTimeField()
    week = models.IntegerField()
    out_isolation = models.FloatField()
    int_temp = models.FloatField()
    int_hum = models.FloatField()
    int_co2 = models.FloatField(db_column='int_CO2')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'environment'


class Growth(models.Model):
    user_number = models.ForeignKey('User', models.DO_NOTHING, db_column='user_number')
    input_date = models.DateTimeField(blank=True, null=True)
    chojang = models.FloatField(blank=True, null=True)
    max_yeopjang = models.FloatField(blank=True, null=True)
    yeaoppok = models.FloatField(blank=True, null=True)
    yeopbyeongjang = models.FloatField(blank=True, null=True)
    yeopsu = models.FloatField(blank=True, null=True)
    stem_thick = models.FloatField(blank=True, null=True)
    fruit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'growth'


class BestFarmMean(models.Model):
    week = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    intemp = models.FloatField(db_column='inTemp')  # Field name made lowercase.
    outtemp = models.FloatField(db_column='outTemp')  # Field name made lowercase.
    inhum = models.FloatField(db_column='inHum')  # Field name made lowercase.
    inco2 = models.FloatField(db_column='inCO2')  # Field name made lowercase.
    acinso = models.FloatField(db_column='acInso')  # Field name made lowercase.
    nsec = models.FloatField(db_column='nsEC')  # Field name made lowercase.
    nsph = models.FloatField(db_column='nspH')  # Field name made lowercase.
    nsweek = models.FloatField(db_column='nsWeek')  # Field name made lowercase.
    best_farm_meancol = models.FloatField()
    pllnlt = models.FloatField(db_column='pllnLt')  # Field name made lowercase.
    lefcunt = models.FloatField(db_column='lefCunt')  # Field name made lowercase.
    leflt = models.FloatField(db_column='lefLt')  # Field name made lowercase.
    lefbt = models.FloatField(db_column='lefBt')  # Field name made lowercase.
    lefstalklt = models.FloatField()
    tcdmt = models.FloatField()
    flwrco = models.FloatField(db_column='flwrCo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'best_farm_mean'
