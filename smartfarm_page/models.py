from django.db import models

# 앱에서 사용하는 데이터 구조를 정의하고 DB와의 소통을 담당하는 파일

from django.db import models


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
