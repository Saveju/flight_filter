import csv
from time import mktime
import datetime

data = input('file name you wish to extract data from: ')
bags_no = input('number of bags? (0/1/2): ')
file = open(data,newline = '')
reader = csv.reader(file)

flight_data = [flight for flight in reader]

if len(flight_data[0][0]) > 3:
    flight_data.pop(0)

def unix_time(data):
    a,b = data.split('T')
    c = a.split('-') + b.split(':')
    y,m,d,hours,mins = [int(date) for date in c[:5]]
    dt = datetime.datetime(y,m,d,hours,mins)
    unixx_time = mktime(dt.timetuple())
    return unixx_time

def times_ok(flight1,flight2):
    if flight1 - flight2 in range(-14400,-3599):
        return True

def loop():
    for flight in flight_data:
        if filtered[-1][-1][-2] <= flight[-2] and times_ok(unix_time(filtered[-1][-1][3]),unix_time(flight[2])) and filtered[-1][-1][1] == flight[0]:
            if flight[0] != filtered[-1][-2][0] and flight[1] != filtered[-1][-2][1]:
                return filtered[-1].append(flight), loop()

filtered = []

for flight in flight_data:
    for f in flight_data:
        if flight[-2] <= f[-2] and times_ok(unix_time(flight[3]),unix_time(f[2])) and flight[1] == f[0]:
            filtered.append([flight,f])
            loop()

with open('combinationss.csv','w',newline='') as f:
    writer = csv.writer(f)

    for fl in filtered:
        total_price = 0
        excessive_bags = list(filter(lambda x:x[-2]<bags_no,fl))
        if not excessive_bags:
            for f in fl:
                writer.writerows([f])
                total_price += (float(f[-3]) + float(f[-1])*float(bags_no))
            writer.writerow(['cost of the itinerary with bags ordered: ' , total_price])

print('result has been stored in combinationss.csv')
