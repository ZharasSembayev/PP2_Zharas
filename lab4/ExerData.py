#1: Выводим вычитания пяти дней из текущего даты:
from  datetime import  datetime, timedelta
today = datetime.today()
new = today - timedelta(days = 5)
print(today.strftime("%Y-%m-%d")) 
print(new.strftime("%Y-%m-%d"))

#2: Выводим вчерашнюю,сегодняшнюю,завтрашнюю:
from datetime import datetime, timedelta
t = datetime.today()
y = t - timedelta(days = 1)
tomorrow = t + timedelta(days = 1)
print(t.strftime("%Y-%m-%d"))
print(y.strftime("%Y-%m-%d"))
print(tomorrow.strftime("%Y-%m-%d"))

#3: Выводим код который отбрасывает микросекунду от дата и времени:
from datetime import datetime
t = datetime.now()
print(t)
new = t.replace(microsecond = 0)
print(new)

#4: Выводим вычисления разницы в две даты за секунду:
from datetime import datetime, timedelta
d1 = datetime.today()
d2 = d1 + timedelta(days = 1)
d1_str = d1.strftime("%Y-%m-%d %H:%M:%S")
d2_str = d2.strftime("%Y-%m-%d %H:%M:%S")
dt1 = datetime.strptime(d1_str, "%Y-%m-%d %H:%M:%S")
dt2 = datetime.strptime(d2_str, "%Y-%m-%d %H:%M:%S")
dif = abs((dt2 - dt1).total_seconds())
print(dif)
