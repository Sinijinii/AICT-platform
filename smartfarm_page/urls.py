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
    path('kids_result/', views.kids_result, name='kids_result'),
    path('kids_result/pick_date', views.pick_date, name="pick_date"),
    path('kids_result/pick_part', views.pick_part, name="pick_part"),
    path('kids_result/pick_month', views.pick_month, name="pick_month"),
    path('kids_data_fileupload/', views.kids_data_fileupload, name="kids_data_fileupload"),
    path('kids_data_fileupload/kids_data_upload', views.kids_data_upload, name="kids_data_upload"),
    path('kids_data_fileupload/input_kids_data', views.input_kids_data, name="input_kids_data"),
    # covid19
    path('covid19/', views.covid19, name='covid19'),
]