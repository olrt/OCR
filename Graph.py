import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates

dates = ['27/07/2023','31/07/2023','24/08/2023']
x = [dt.datetime.strptime(d,'%d/%m/%Y').date() for d in dates]
plt.xlim([dt.date(2023, 7, 1), dt.date(2023, 10, 31)])

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=20))
plt.gcf().autofmt_xdate()

plt.axhline(y = 136, color = 'r', linestyle = '-')
plt.axhline(y = 145, color = 'r', linestyle = '-')
y=[140, 138, 142]
plt.ylim(120, 160)
plt.plot(x,y,markerfacecolor='Blue', marker='.')
plt.xlabel('Result Date')
plt.ylabel('Sodium Level')
plt.title("Sodium graph")
plt.show()