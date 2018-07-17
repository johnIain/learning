import datetime
s='2014-01-05'
print (str(int(datetime.datetime.strptime(s,'%Y-%m-%d').strftime("%j")))+' '+str(int(datetime.datetime.strptime(s,'%Y-%m-%d').strftime("%U"))+1))