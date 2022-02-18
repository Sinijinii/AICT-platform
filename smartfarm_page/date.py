from django import date
from .models import AllKids
from .models import All
all_data =  pd.DataFrame(list(All.objects.filter(day=date_).values('heartrate', 'sc_field', 'error', 'zsc', 'day', 'time', 'week','km','cal','date')))
    all_data = all_data.fillna(value=0)
    data_date = pd.DataFrame(list(All.objects.filter(day=date_,name=Name2 ).values('heartrate', 'sc_field', 'error', 'zsc', 'day', 'time', 'week','name','km','cal','date')))
    data_date = data_date.fillna(value=0)
if All.objects.filter(name=Name2, day=date_).exists():
    not_exist = False
else:
    not_exist = True
# 개인 1시간 평균
h_data = data_date.set_index('date')
h_dat2 = h_data.resample('1H').mean()
h_dat2 = h_dat2.reset_index()
h_dat2['time'] = h_dat2['date'].dt.hour
# 전체 1시간 평균
all_ = all_data.set_index('date')
all2 = all_.resample('1H').mean()
all2 = all2.reset_index()
all2['time'] = all2['date'].dt.hour
aaaa = pd.DataFrame()
aaaa['time'] = [10, 11, 12, 13, 14, 15, 16]
aaaa = pd.merge(aaaa, h_dat2, on='time', how='left')
aaaa = pd.merge(aaaa, all2, on='time', how='left')
aaaa = aaaa.fillna(value=0)
print(aaaa)
# 개인 정보
# day_kid =list(aaaa['time_x'].astype('str'))
hr_kid = list(aaaa['heartrate_x'])
sc_kid = list(aaaa['sc_field_x'])
zsc_kid = list(aaaa['zsc_x'])
km_kid = list(aaaa['km_x'])
cal_kid = list(aaaa['cal_x'])
# 전체 정보
# day_all = list(aaaa['time_y'].astype('str'))
hr_all = list(aaaa['heartrate_y'])
sc_all = list(aaaa['sc_field_y'])
zsc_all = list(aaaa['zsc_y'])
km_all = list(aaaa['km_y'])
cal_all = list(aaaa['cal_y'])
## 전체평균
HR_all = numpy.mean(list(all_data["heartrate"]))
# print(week)
print(date_)
# print(aaaa)
print(sc_kid)
return render(request, 'result.html', {"name": Name2, "birth": birth, "a": a, "not_exist": not_exist,
                                       "hr_kid": hr_kid, "sc_kid": sc_kid, "zsc_kid": zsc_kid, "km_kid": km_kid,
                                       "cal_kid": cal_kid,
                                       "hr_all": hr_all, "sc_all": sc_all, "zsc_all": zsc_all, "km_all": km_all,
                                       "cal_all": cal_all})





mon_all = pd.DataFrame(list(All.objects.filter(week="mon").values('heartrate', 'sc_field', 'error', 'zsc', 'day', 'time', 'week', 'km','cal', 'date')))
        tue_all = pd.DataFrame(list(All.objects.filter(week="tue").values('heartrate', 'sc_field', 'error', 'zsc', 'day', 'time', 'week', 'km','cal', 'date')))
        wend_all = pd.DataFrame(list(All.objects.filter(week="wen").values('heartrate', 'sc_field', 'error', 'zsc', 'day', 'time', 'week', 'km','cal', 'date')))
        thu_all = pd.DataFrame(list(All.objects.filter(week="thu").values('heartrate', 'sc_field', 'error', 'zsc', 'day', 'time', 'week', 'km','cal', 'date')))
        fri_all = pd.DataFrame(list(All.objects.filter(week="fri").values('heartrate', 'sc_field', 'error', 'zsc', 'day', 'time', 'week', 'km','cal', 'date')))
        mon_all = mon_all.fillna(value=0)
        tue_all = tue_all.fillna(value=0)
        wend_all = wend_all.fillna(value=0)
        thu_all = thu_all.fillna(value=0)
        fri_all = fri_all.fillna(value=0)
        mon_data = pd.DataFrame(list(All.objects.filter(week="mon", name=Name2).values('heartrate', 'sc_field', 'error', 'zsc', 'day', 'time','week', 'name', 'km', 'cal', 'date')))
        tue_data = pd.DataFrame(list(All.objects.filter(week="tue", name=Name2).values('heartrate', 'sc_field', 'error', 'zsc', 'day', 'time','week', 'name', 'km', 'cal', 'date')))
        wend_data = pd.DataFrame(list(All.objects.filter(week="wen", name=Name2).values('heartrate', 'sc_field', 'error', 'zsc', 'day', 'time','week', 'name', 'km', 'cal', 'date')))
        thu_data = pd.DataFrame(list(All.objects.filter(week="thu", name=Name2).values('heartrate', 'sc_field', 'error', 'zsc', 'day', 'time','week', 'name', 'km', 'cal', 'date')))
        fri_data = pd.DataFrame(list(All.objects.filter(week="fri", name=Name2).values('heartrate', 'sc_field', 'error', 'zsc', 'day', 'time','week', 'name', 'km', 'cal', 'date')))
        mon_data = mon_data.fillna(value=0)
        tue_data = tue_data.fillna(value=0)
        wend_data = wend_data.fillna(value=0)
        thu_data = thu_data.fillna(value=0)
        fri_data = fri_data.fillna(value=0)
        if All.objects.filter(name=Name2).exists():
            not_exist = False
        else:
            not_exist = True
        # 개인 1시간 평균
        # 월요일
        m_data = mon_data.set_index('date');m_dat2 = m_data.resample('1H').mean()
        m_dat2 = m_dat2.reset_index()
        m_dat2['time'] = m_dat2['date'].dt.hour
        # 화요일
        tu_data = tue_data.set_index('date')
        tu_dat2 = tu_data.resample('1H').mean()
        tu_dat2 = tu_dat2.reset_index()
        tu_dat2['time'] = tu_dat2['date'].dt.hour
        print(tu)
        # 수요일
        w_data = wend_data.set_index('date')
        w_dat2 = w_data.resample('1H').mean()
        w_dat2 = w_dat2.reset_index()
        w_dat2['time'] = w_dat2['date'].dt.hour
        # 목요일
        th_data = thu_data.set_index('date')
        th_dat2 = th_data.resample('1H').mean()
        th_dat2 = th_dat2.reset_index()
        th_dat2['time'] = th_dat2['date'].dt.hour
        # 금요일
        f_data = fri_data.set_index('date')
        f_dat2 = f_data.resample('1H').mean()
        f_dat2 = f_dat2.reset_index()
        f_dat2['time'] = f_dat2['date'].dt.hour

        # 전체 1시간 평균
        # 월요일
        m_all = mon_all.set_index('date');
        m_all2 = m_data.resample('1H').mean()
        m_all2 = m_all2.reset_index()
        m_all2['time'] = m_all2['date'].dt.hour
        # 화요일
        tu_all= tue_all.set_index('date')
        tu_all2 = tu_all.resample('1H').mean()
        tu_all2 = tu_all2.reset_index()
        tu_all2['time'] = tu_all2['date'].dt.hour
        # 수요일
        w_all = wend_all.set_index('date')
        w_all2 = w_all.resample('1H').mean()
        w_all2 = w_all2.reset_index()
        w_all2['time'] = w_all2['date'].dt.hour
        # 목요일
        th_all = thu_all.set_index('date')
        th_all2 = th_all.resample('1H').mean()
        th_all2 = th_all2.reset_index()
        th_all2['time'] = th_all2['date'].dt.hour
        # 금요일
        f_all = fri_all.set_index('date')
        f_all2 = f_all.resample('1H').mean()
        f_all2 = f_all2.reset_index()
        f_all2['time'] = f_all2['date'].dt.hour