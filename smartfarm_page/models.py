from django.db import models

# 앱에서 사용하는 데이터 구조를 정의하고 DB와의 소통을 담당하는 파일

from django.db import models


class FileUploadModel(models.Model):
    file = models.FileField(upload_to="")


class InputValueModel(models.Model):
    chojang = models.FloatField()
