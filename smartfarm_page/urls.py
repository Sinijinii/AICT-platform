from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('str_smartfarm1/', views.str_smartfarm1, name='str_smartfarm1'),
    path('kids_pattern1/', views.kids_pattern1, name='kids_pattern1'),
    path('finedust1/', views.finedust1, name='finedust1'),
    path('fileupload/', views.upload_file, name="fileupload"),
    path('input_value/', views.input_value, name="input_value"),
    path('str_smartfarm2/', views.str_smartfarm2, name='str_smartfarm2'),
    path('demographics/', views.demographics, name='demographics'),
    path('result/', views.result, name='result')
]