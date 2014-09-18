import requests

f = open('samplenew.csv','rU')
contents = f.read().split('\n')
url = 'http://services.odata.org/Northwind/Northwind.svc/Products/$count?$filter='
newcontents = []

for thing in contents:
	newcontents.append(url+thing)

for thing in newcontents:
	print requests.get(thing).text

