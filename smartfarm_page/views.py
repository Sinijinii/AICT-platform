from django.shortcuts import render, redirect

# 앱에서 어떤 기능을 할지에 대한 메인 로직을 담당하는 파일

# open urls
def index(request):
    return render(request, 'index.html')

def str_smartfarm1(request):
    return render(request, 'str_smartfarm1.html')

def kids_pattern1(request):
    return render(request, 'kids_pattern1.html')

def covid19(request):
    return render(request, 'covid19.html')

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


# 가장 생성시각이 큰(가장 최근인) 파일을 리턴
def recent_file():
    media_path = "./media/"
    each_file_path_and_gen_time = []
    for each_file_name in os.listdir(media_path):
        each_file_path = media_path + each_file_name
        each_file_gen_time = os.path.getctime(each_file_path)  # getctime: 입력받은 경로에 대한 생성 시간을 리턴
        each_file_path_and_gen_time.append(
            (each_file_path, each_file_gen_time)
        )
    most_recent_file = max(each_file_path_and_gen_time, key=lambda x: x[1])[0]
    return most_recent_file

import numpy as np

# 사용자가 직접 입력한 생육변수 데이터 가져와서 예측값 return
def input_value(request):
    if request.method == 'POST':
        week1 = request.POST.getlist('week1[]')
        week1 = list(map(float, week1))
        week2 = request.POST.getlist('week2[]')
        week2 = list(map(float, week2))

        result = data_analysis(week1, week2)

        # 그래프 그리기 위해 해당 농가 환경변수 data 정리
        most_recent_file = recent_file()
        df = pd.read_excel(most_recent_file)
        myFarm_date = list(df['주차'])
        # date = [dd.strftime('%Y-%m-%d') for dd in date]
        acInso = list(np.round(list(df['외부 일사량']), 2))
        inTemp = list(np.round(list(df['내부온도']), 2))
        inHum = list(np.round(list(df['내부습도']), 2))
        inCO2 = list(np.round(list(df['내부CO2']), 2))
        myFarm_dict = {'date': myFarm_date, 'acInso': acInso, 'inTemp': inTemp, 'inHum': inHum, 'inCO2': inCO2}

        # 우수 농가 환경변수 data 정리
        df = pd.read_excel('./smartfarm_page/static/smartfarm_page/assets/웹 시험용 기본농가 우수 평균 데이터셋.xlsx')
        date = list(df['주차'])
        # date = [dd.strftime('%Y-%m-%d') for dd in date]
        ## label을 기본농가 시작점 ~ 우수농가 끝점으로 맞추기
        start = date.index(myFarm_date[0])
        date = date[start:]
        acInso = list(np.round(list(df['외부 일사량']), 2))
        inTemp = list(np.round(list(df['내부온도']), 2))
        inHum = list(np.round(list(df['내부습도']), 2))
        inCO2 = list(np.round(list(df['내부CO2']), 2))
        bestFarm_dict = {'date': date, 'acInso': acInso, 'inTemp': inTemp, 'inHum': inHum, 'inCO2': inCO2}

        return render(request, 'str_smartfarm2.html', context={'predict_result': result, 'graph_data': myFarm_dict, 'bestFarm_data': bestFarm_dict})

    else:
        return render(request, 'str_smartfarm1.html')


import os
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler

# trained model 가져와 predict 해서 착과수 예측
def data_analysis(week1, week2):
    # 사용자가 업로드한 가장 최근 파일 가져오기
    most_recent_file = recent_file()

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

# API 명세서 한글 파일 다운로드 기능
from django.http import HttpResponse
import mimetypes
import urllib

def download_API_file(request):
    file_path = './smartfarm_page/static/smartfarm_page/assets/공공융합플랫폼 API 기술명세서.hwp'
    file_name = '공공융합플랫폼 API 기술명세서.hwp'
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            quote_file_url = urllib.parse.quote(file_name.encode('utf-8'))
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_name))
            response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
            return response

# 네이버 뉴스 크롤링
import requests
from bs4 import BeautifulSoup

def news_crawling(request):
    raw = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=코로나",
                       headers={'User-Agent': 'Mozilla/5.0'}, verify=False)
    html = BeautifulSoup(raw.text, "html.parser")
    articles = html.select("ul.list_news > li")

    news_lst = []
    num = 0
    for ar in articles:
        num += 1
        title = ar.select_one("a.news_tit").text
        time = ar.select_one("span.info").text
        link = ar.select_one("a.news_tit")['href']
        news_lst.append([title, time, link])
        if num == 5:
            break
    return news_lst


