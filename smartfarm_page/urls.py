from django.urls import path
from requests import request

from . import views
urlpatterns = [
    path('', views.index, name='main'),
    # str_smartfarm
    path('str_smartfarm1/', views.str_smartfarm1, name='str_smartfarm1'),
    path('input_number/', views.input_number, name="input_number"),
    path('ex_xlsx_download/', views.download_ex_file, name="ex_xlsx_download"),
    path('fileupload/', views.upload_file, name="fileupload"),
    path('input_value/', views.input_value, name="input_value"),
    path('str_smartfarm2/', views.str_smartfarm2, name='str_smartfarm2'),
    path('API_doc_download/', views.download_API_file, name="API_doc_download"),
    path('str_smartfarm1/str_smartfarm2/', views.str_smartfarm2, name='str_smartfarm2'),
    # kids_pattern
    path('kids_pattern1/', views.kids_pattern1, name='kids_pattern1'),
    path('result/', views.result, name='result'),
    path('result/pick_date', views.pick_date, name="pick_date"),
    path('result/pick_part', views.pick_part, name="pick_part"),
    path('result/pick_month', views.pick_month, name="pick_month"),
    path('kid_data_fileupload/', views.kid_data_fileupload, name="kid_data_fileupload"),
    path('kid_data_fileupload/kid_data_upload', views.kid_data_upload, name="kid_data_upload"),
    path('kid_data_fileupload/input_kid_data', views.input_kid_data, name="input_kid_data"),
    # covid19
    path('covid19/', views.covid19, name='covid19'),
]