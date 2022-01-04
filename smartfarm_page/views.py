from django.shortcuts import render, redirect

# 앱에서 어떤 기능을 할지에 대한 메인 로직을 담당하는 파일

# open urls
def index(request):
    return render(request, 'index.html')

def str_smartfarm1(request):
    return render(request, 'str_smartfarm1.html')

def kids_pattern1(request):
    return render(request, 'kids_pattern1.html')

def finedust1(request):
    return render(request, 'finedust1.html')

def str_smartfarm2(request):
    return render(request, 'str_smartfarm2.html')

# file upload
from django.shortcuts import render
from .forms import FileUploadForm
from .models import FileUploadModel
from .models import InputValueModel

def upload_file(request):
    if request.method == 'POST':        # POST 방식이면, 데이터가 담긴 제출된 form으로 간주
        file = request.FILES['uploadFromPC']
        uploadFile = FileUploadModel(
            file=file,
        )
        uploadFile.save()
        return redirect('fileupload')
    else:
        fileuploadForm = FileUploadForm
        context = {
            'fileuploadForm': fileuploadForm,
        }
        return render(request, 'str_smartfarm1.html', context)

def input_value(request):
    if request.method == 'POST':
        week1 = request.POST.getlist('week1[]')
        week1 = list(map(float, week1))
        week2 = request.POST.getlist('week2[]')
        week2 = list(map(float, week2))

        result = data_analysis(week1, week2)
        return render(request, 'str_smartfarm2.html', {'predict_result': result})

    else:
        return render(request, 'str_smartfarm1.html')

# trained model 가져와 predict 해서 착과수 예측
import os
import pandas as pd
import numpy as np
import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler

def data_analysis(week1, week2):
    # 사용자가 업로드한 가장 최근 파일 가져오기
    media_path = "./media/"
    each_file_path_and_gen_time = []
    for each_file_name in os.listdir(media_path):
        each_file_path = media_path + each_file_name
        each_file_gen_time = os.path.getctime(each_file_path)        # getctime: 입력받은 경로에 대한 생성 시간을 리턴
        each_file_path_and_gen_time.append(
            (each_file_path, each_file_gen_time)
        )
    # 가장 생성시각이 큰(가장 최근인) 파일을 리턴
    most_recent_file = max(each_file_path_and_gen_time, key=lambda x: x[1])[0]

    # 데이터셋 생성
    df = pd.read_excel(most_recent_file)
    env_set = df.drop(columns=['시설ID', '수집일', '주차']).values
    growth_set = np.array([week1, week2])
    to_pred_data = np.hstack((env_set[-2:], growth_set))

    ### Feature Scaling
    sc = StandardScaler()       # 입력 기능용 스케일러
    data_scaled = sc.fit_transform(to_pred_data)
    sc_predict = StandardScaler()       # 예측 대상용 스케일러
    sc_predict.fit_transform(to_pred_data[:, 10:11])

    X_test = []
    X_test.append(data_scaled)
    X_test = np.array(X_test)

    ### Predict
    model = load_model('./smartfarm_page/static/smartfarm_page/assets/LSTM_model.h5')
    predictions_future = model.predict(X_test)

    ### scaled -> actual
    y_pred_future = sc_predict.inverse_transform(predictions_future)
    result = y_pred_future[0][0]
    return round(result, 2)
