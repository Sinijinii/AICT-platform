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

class Str_user(models.Model):
    user_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        app_label = 'default'
        db_table = 'user'

    def __str__(self):
        return self.user_id

class Environment(models.Model):
    user_num = models.OneToOneField('Str_user', models.DO_NOTHING, db_column='user_num', primary_key=True)
    farm_id = models.CharField(max_length=45)
    date = models.DateTimeField()
    week = models.IntegerField()
    out_isolation = models.FloatField()
    int_temp = models.FloatField()
    int_hum = models.FloatField()
    int_co2 = models.FloatField(db_column='int_CO2')  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'default'
        db_table = 'environment'

class Growth(models.Model):
    user_number = models.ForeignKey('Str_user', models.DO_NOTHING, db_column='user_number')
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
        app_label = 'default'
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
        app_label = 'default'
        db_table = 'best_farm_mean'


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