import psutil
conns = psutil.net_connections(kind ='tcp')
filteredConns = [c for c in conns if (str(c.raddr) != '()' and str(c.laddr) != '()' and str(c.pid) != 'None')]
conList =  map(list, filteredConns)
for sublist in conList: 
   del sublist[:3]  
from operator import itemgetter
from itertools import groupby
conList = sorted(conList, key=itemgetter(3))
newConList = []
for i in conList:
    i[0] =str(i[0][0]) +"@"+ str(i[0][1])
    i[1] =str(i[1][0]) +"@"+ str(i[1][1])  
    newConList.append(i)
if (len(newConList) > 0):
    grpList = {k:list(val) for k, val in groupby(newConList, key = itemgetter(3))}
    print "\"pid\",","\"laddr\",", "\"raddr\",", "\"status\""
    for k in sorted(grpList, key=lambda k: len(grpList[k]), reverse=True):
        for gl in grpList[k]:
             print ('"{0}",'.format(k)),','.join('"{0}"'.format(x) for x in gl[:3])
else:
    print "\"No TCP Sockets found\""
