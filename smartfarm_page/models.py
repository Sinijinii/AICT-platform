from django.core.validators import RegexValidator
from django.db import models

# str_smartfarm
class Str_user(models.Model):
    phoneNumberRegex = RegexValidator(regex=r'?([0-9]{3,4})-?([0-9]{4})$')
    user_id = models.CharField(validators=[phoneNumberRegex], primary_key=True, max_length=8)

    class Meta:
        managed = False
        app_label = 'default'
        db_table = 'str_user'

    def __str__(self):
        return self.user_id

class Environment(models.Model):
    env_index = models.AutoField(primary_key=True)
    user_num = models.ForeignKey('Str_user', models.CASCADE, db_column='user_num')
    farm_id = models.CharField(max_length=45)
    date = models.DateTimeField()
    week = models.IntegerField()
    out_isolation = models.FloatField()
    in_temp = models.FloatField()
    in_hum = models.FloatField()
    in_co2 = models.FloatField(db_column='in_CO2')
    input_time = models.DateTimeField() # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'default'
        db_table = 'environment'

class Growth(models.Model):
    user_number = models.ForeignKey('Str_user', models.CASCADE, db_column='user_number')
    input_time = models.DateTimeField()
    chojang = models.FloatField()
    max_yeopjang = models.FloatField()
    yeaoppok = models.FloatField()
    yeopbyeongjang = models.FloatField()
    yeopsu = models.FloatField()
    stem_thick = models.FloatField()
    fruit = models.FloatField()

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

class PredictResult(models.Model):
    pred_index = models.AutoField(primary_key=True)
    user_code = models.ForeignKey('Str_user', models.CASCADE, db_column='user_code')
    lstm_result = models.FloatField()
    predict_date = models.DateTimeField()

    class Meta:
        managed = False
        app_label = 'default'
        db_table = 'predict_result'

# kids pattern
class All(models.Model):
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
    cal = models.IntegerField(db_column='Cal')
    km = models.IntegerField(db_column='Km')

    class Meta:
        managed = False
        app_label = 'kids_db'
        db_table = 'kids_data'
        unique_together = (('id', 'name'),)

class AllKids(models.Model):
    번호 = models.IntegerField()
    name = models.CharField(db_column='Name',primary_key=True, max_length=5)
    생년월일 = models.DateField(blank=True, null=True)
    반 = models.CharField(max_length=12, blank=True, null=True)
    성별 = models.CharField(max_length=5, blank=True, null=True)
    성향 = models.CharField(max_length=5, blank=True, null=True)
    #b_id = models.CharField(db_column="밴드_ID", max_length=25)  # Field name made lowercase.
    어린이집 = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'kids_db'
        db_table = 'all_kids'
        unique_together = (('name'),)