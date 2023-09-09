from datetime import datetime

a='Sodium 123.1 mmol'
word='Sodium'
count=len(word)
b=a.find(word)+count
#[0:count]
print (b)
print (a[b:].strip())

s = "41 yeas"
t=s.replace(" years", "")
print(t)

data = "11-Sep-1981"
dateFormat = "%d-%b-%Y"
#newDateFormat = "%Y-%m-%d"
try:
    dt = bool(datetime.strptime(data, dateFormat))
    dt = datetime.strptime(data, dateFormat).date()
    #dt = datetime.strptime(data, "%Y-%m-%d").date()
    print (type(dt))
    print (dt)
    #dt = datetime.strftime(dt, newDateFormat)
    #print (type(dt))
    #print (dt)
    #dt = datetime.strptime(dt, newDateFormat).date()
    #print (type(dt))
    #print (dt)
    #dt = datetime.strptime(data, dateFormat).date()
    
    #print (dt)
except ValueError:
    dt = None
    #dt = datetime.strptime("0000-", dateFormat).date()
    print (type(dt))
    print (dt)