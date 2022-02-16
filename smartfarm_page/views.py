from django.shortcuts import render, redirect
from .models import AllKids
from .models import All

# 앱에서 어떤 기능을 할지에 대한 메인 로직을 담당하는 파일

# open urls
def index(request):
    return render(request, 'index.html')

def str_smartfarm1(request):
    return render(request, 'str_smartfarm1.html')

def kids_pattern1(request):
    return render(request, 'kids_pattern1.html')

def covid19(request):
    graph_dict = covid_graph()
    news_lst = news_crawling()
    return render(request, 'covid19.html', context={'graph_dict':graph_dict, 'news_lst':news_lst})

def str_smartfarm2(request):
    return render(request, 'str_smartfarm2.html')

## kids_pattern
def result(request):
    students = AllKids.objects.values()
    Name = request.POST['name']
    center = request.POST['C_name']
    class_ = request.POST['class']
    birth = request.POST['password']
    a=AllKids.objects.filter(이름=Name).values('이름','어린이집','반','생년월일','성별','성향')
    if AllKids.objects.filter(이름=Name, 어린이집=center, 반=class_, 생년월일=birth).exists():
        not_exist = False
    else:
        not_exist = True

    if AllKids.objects.filter(성별='남'):
        boy = True
    else:
        boy = False

    if AllKids.objects.filter(성향='외향적'):
        E = True
    else:
        E = False

    # 측정정보
    kid_d = All.objects.filter(name=Name).values('heartrate', 'sc_field', 'error', 'zsc', 'day', 'time', 'week','name')
    Heartrate=All.objects.filter(name=Name).values('day','time','heartrate')
    step = All.objects.filter(name=Name).values('sc_field')
    day = All.objects.filter(name=Name).values('day')
    time = All.objects.filter(name=Name).values('time')
    week = All.objects.filter(name=Name).values('week')
    return render(request, 'result.html', {"students": students, "name":Name,"not_exist":not_exist,"birth":birth,"a":a, "boy":boy,"E":E,
                                           "kid_d":kid_d,"heartrate":Heartrate,"step":step,"day":day,"time":time,"week":week})

## str_smartfarm
# file upload
from django.shortcuts import render
from django.utils import timezone
import copy

# ID(phone number) 전역변수로 할당
phone_id = '0'
now = timezone.now()

from .models import Environment
from django.conf import settings
import io
from sqlalchemy import create_engine

def upload_file(request):
    if request.method == 'POST':        # POST 방식이면, 데이터가 담긴 제출된 form으로 간주
        file = request.FILES['uploadFromPC'].file
        data_df = file
        try:
            data_df = pd.read_excel(io.BytesIO(file.read()))
        except:
            render(request, 'str_smartfarm1.html')

        data_df['user_num'] = phone_id
        global now
        now = timezone.now()
        now = copy.deepcopy(now)
        data_df['input_time'] = now

        data_df = data_df[['user_num', '시설ID', '수집일', '주차', '외부 일사량', '내부온도', '내부습도', '내부CO2', 'input_time']]
        data_df.rename(columns = {'시설ID':'farm_id', '수집일':'date', '주차':'week', '외부 일사량':'out_isolation', '내부온도':'in_temp', '내부습도':'in_hum', '내부CO2':'in_CO2'}, inplace=True)
        database_url = 'mysql://{user}:{password}@localhost/{database_name}'.format(
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            database_name=settings.DATABASES['default']['NAME'],
        )
        engine = create_engine(database_url, echo=False)
        data_df.to_sql(name='environment', con=engine, index=False, if_exists='append')
        return redirect('fileupload')
    else:
        return render(request, 'str_smartfarm1.html')

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


# 사용자가 직접 입력한 생육변수 데이터 가져와서 db에 저장 후 예측값 return
from .models import Growth
from .models import BestFarmMean
import numpy as np
from datetime import timedelta

def input_value(request):
    if request.method == 'POST':
        week1 = request.POST.getlist('week1[]')
        week1 = list(map(float, week1))
        week2 = request.POST.getlist('week2[]')
        week2 = list(map(float, week2))

        # 데이터 DB Growth 테이블에 저장
        user_obj = Str_user.objects.get(user_id = phone_id)
        farm_grow_1 = Growth(user_number=user_obj, input_time=now, chojang=week1[0],
                             max_yeopjang=week1[1], yeaoppok=week1[2],
                             yeopbyeongjang=week1[3], yeopsu=week1[4],
                             stem_thick=week1[5], fruit=week1[6])
        farm_grow_2 = Growth(user_number=user_obj, input_time=now, chojang=week2[0],
                             max_yeopjang=week2[1], yeaoppok=week2[2],
                             yeopbyeongjang=week2[3], yeopsu=week2[4],
                             stem_thick=week2[5], fruit=week2[6])
        farm_grow_1.save()
        farm_grow_2.save()

        result = data_analysis(week1, week2)

        # 그래프 그리기 위해 해당 농가 환경변수 data 정리
        env_data = Environment.objects.filter(
            Q(user_num=phone_id) & Q(input_time__range=[now - timedelta(seconds=1), now + timedelta(seconds=1)]))
        df = read_frame(env_data)
        myFarm_date = list(df['week'])
        acInso = list(np.round(list(df['out_isolation']), 2))
        inTemp = list(np.round(list(df['in_temp']), 2))
        inHum = list(np.round(list(df['in_hum']), 2))
        inCO2 = list(np.round(list(df['in_co2']), 2))
        myFarm_dict = {'date': myFarm_date, 'acInso': acInso, 'inTemp': inTemp, 'inHum': inHum, 'inCO2': inCO2}

        # 우수 농가 환경변수 data 정리
        bestfarm_data = BestFarmMean.objects.all()
        df = read_frame(bestfarm_data)
        date = list(df['week'])
        # date = [dd.strftime('%Y-%m-%d') for dd in date]
        ## label을 기본농가 시작점 ~ 우수농가 끝점으로 맞추기
        start = date.index(myFarm_date[0])
        date = date[start:]
        acInso = list(np.round(list(df['acinso']), 2))
        acInso = acInso[start:]
        inTemp = list(np.round(list(df['intemp']), 2))
        inTemp = inTemp[start:]
        inHum = list(np.round(list(df['inhum']), 2))
        inHum = inHum[start:]
        inCO2 = list(np.round(list(df['inco2']), 2))
        inCO2 = inCO2[start:]
        bestFarm_dict = {'date': date, 'acInso': acInso, 'inTemp': inTemp, 'inHum': inHum, 'inCO2': inCO2}

        return render(request, 'str_smartfarm2.html', context={'predict_result': result, 'graph_data': myFarm_dict, 'bestFarm_data': bestFarm_dict})

    else:
        return render(request, 'str_smartfarm1.html')

import os
import pandas as pd
from django.db.models import Q
from django_pandas.io import read_frame
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler

# trained model 가져와 predict 해서 착과수 예측
def data_analysis(week1, week2):
    # DB에서 사용자가 업로드한 데이터 가져오기 - 범위 : 2sec
    env_data = Environment.objects.filter(Q(user_num=phone_id) & Q(input_time__range=[now - timedelta(seconds=1), now + timedelta(seconds=1)]))
    df = read_frame(env_data)

    # 데이터셋 생성
    env_set = df.drop(columns=['env_index', 'user_num', 'farm_id', 'date', 'week', 'input_time']).values
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

def download_ex_file(request):
    file_path = './smartfarm_page/static/smartfarm_page/assets/환경변수 데이터셋 Sample.xlsx'
    file_name = '환경변수 데이터셋 Sample.xlsx'
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            quote_file_url = urllib.parse.quote(file_name.encode('utf-8'))
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_name))
            response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
            return response

# 네이버 뉴스 크롤링
import requests
from bs4 import BeautifulSoup

def news_crawling():
    raw = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=코로나",
                       headers={'User-Agent': 'Mozilla/5.0'}, verify=False)
    html = BeautifulSoup(raw.text, "html.parser")
    articles = html.select("ul.list_news > li")

    news_lst = []
    num = 0
    for ar in articles:
        try:    # 기사 이미지 없는 경우 pass
            image = ar.select_one('div > a > img')['src']
        except:
            continue
        title = ar.select_one("a.news_tit").text
        time = ar.select_one("span.info").text
        link = ar.select_one("a.news_tit")['href']
        pub = ar.select_one("a.info").text.split(' ')[0].replace('언론사', '')
        image = ar.select_one('div > a > img')['src']
        if pub == '스포츠동아':
            continue
        news_lst.append({'title':title, 'pub':pub, 'time':time, 'link':link, 'image':image})
        num += 1
        if num == 6:
            break
    return news_lst

# 코로나 확진자수 api 데이터 가져오기
import time
from dateutil.parser import parse
from urllib.parse import unquote
import xml.etree.ElementTree as el
import pandas as pd
import xml.etree.ElementTree as ET
import datetime

def covid_graph():
    serviceURL = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson'
    # 인증키
    serviceKey = 'wJJLUr7wt7dy1QImckWHqfneTIXSE7zW+O9NBD3289VJUF7tCq4XdyIhvS2vSXGEXDWDg/8ysAK0vYYQZfh+wg=='
    # 서비스키가 utf8로 인코딩되어 있어서 unquote로 디코딩에서 get요청을 보내야 응답이 정상적으로 옵니다.
    serviceKey_decode = unquote(serviceKey)

    pageNo = '2'
    numOfRows = '10'
    startCreateDt = '20220101'
    endCreateDt = time.strftime('%Y%m%d', time.localtime(time.time()))
    # api문서대로 파라미터를 설정합니다
    parameters = {"serviceKey": serviceKey_decode, "pageNo": pageNo, "numOfRows": numOfRows,
                  "startCreateDt": startCreateDt, "endCreateDt": endCreateDt}

    # get요청을 보냅니다.
    response = requests.get(serviceURL, params=parameters)

    # 200이면 서버응답이 제대로 되었다는 뜻
    if response.status_code == 200:
        tree = ET.fromstring(response.text)
        iter = tree.iter(tag="item")

        df = pd.DataFrame()

        for element in iter:
            element_dict = {}

            element_dict['일시'] = element.find('createDt').text  # 일시
            element_dict['사망자 수'] = element.find('deathCnt').text  # 사망자
            element_dict['시도명'] = element.find('gubun').text  # 지역
            element_dict['전일대비 증감'] = element.find('incDec').text  # 전일대비증감수
            element_dict['확진자 수'] = element.find('defCnt').text  # 확진자수
            element_dict['격리해제 수'] = element.find('isolClearCnt').text  # 격리해제수
            element_dict['지역발생 수'] = element.find('localOccCnt').text  # 지역발생수
            element_dict['해외유입'] = element.find('overFlowCnt').text  # 해외유입수
            element_dict['10만명당 발생률'] = element.find('qurRate').text  # 10만명당 발생률
            element_dict['id'] = element.find('seq').text  # 게시글 번호(고유값)
            element_dict['기준일시'] = element.find('stdDay')  # 기준일시
            df = df.append(element_dict, ignore_index=True)

        df['일시'] = pd.to_datetime(df['일시'], format="%Y %m %d")
        df['사망자 수'] = pd.to_numeric(df['사망자 수'])
        df['전일대비 증감'] = pd.to_numeric(df['전일대비 증감'])
        df['확진자 수'] = pd.to_numeric(df['확진자 수'])
        df['격리해제 수'] = pd.to_numeric(df['격리해제 수'])
        df['지역발생 수'] = pd.to_numeric(df['지역발생 수'])
        df['해외유입'] = pd.to_numeric(df['해외유입'])
        # df['10만명당 발생률'] = pd.to_numeric(df['10만명당 발생률'])

        df['일시'] = df["일시"].dt.strftime("%Y-%m-%d")

        now = datetime.now()
        nowDate = now.strftime('%Y-%m-%d')

        total_covid_df = df.query("(시도명 == '합계') and (일시 == @nowDate)")

        if total_covid_df.empty:
            yesterday = (now - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
            total_covid_df = df.query("(시도명 == '합계') and (일시 == @yesterday)")

        total_num = total_covid_df['확진자 수'].iloc[0]
        region_num = total_covid_df['지역발생 수'].iloc[0]
        abroad_num = total_covid_df['해외유입'].iloc[0]
        today_total_num = region_num + abroad_num

        change_covid_df = df.query("시도명 == '합계'")
        change_covid_date = list( change_covid_df['일시'])
        change_covid_patient = list(change_covid_df['확진자 수'])
        today_acc_covid_patient = change_covid_patient[0]

        covid_graph_dict = {'covid_total' : format(total_num,',d'), 'region_num' : region_num, 'abroad_num': format(abroad_num, ',d'), 'today_total_num': format(today_total_num,',d'), 'change_covid_date' :change_covid_date[::-1],
                                                         'change_covid_patient' : change_covid_patient[::-1], "today_acc_covid_patient" : format(today_acc_covid_patient,',d')}
        return covid_graph_dict

from .models import Str_user

def input_number(request):
    global phone_id
    if request.method == 'POST':
        phone_id = request.POST.get('phone_number')
        try:
            user_num = Str_user.objects.get(user_id = phone_id)
        except Str_user.DoesNotExist:
            user_num = Str_user(user_id = phone_id)
            user_num.save()
        # auth.login(request, user)
    return render(request, 'str_smartfarm1.html',{"phone_number":phone_id})