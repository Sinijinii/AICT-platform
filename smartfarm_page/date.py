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