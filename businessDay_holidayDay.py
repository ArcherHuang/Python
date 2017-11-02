from business_calendar import Calendar, MO, TU, WE, TH, FR
import datetime
import calendar

year = 2018
month = 12
businessDayCount = 0
holidayDayCount = 0

monthRange = calendar.monthrange(year,month)
cal = Calendar()

for i in range(1,monthRange[1]+1):
	date1 = datetime.datetime(year,month,i) 
	if cal.isbusday(date1):
		# print('%s   : %s' % (i, "Business Day"))
		businessDayCount +=1
	else:
		# print('%s   : %s' % (i, "Holiday Day"))
		holidayDayCount +=1

print('Year        : %s' % year)
print('Month       : %s' % month)
print('Business Day: %s days' % (businessDayCount))
print('Holiday Day : %s days' % (holidayDayCount))
print('Total Day   : %s days' % (monthRange[1]))