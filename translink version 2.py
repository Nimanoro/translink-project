#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#importing required libraries
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen, Request
import json
import ssl

# ignoring security certificate errors
ctx= ssl.create_default_context()
ctx.check_hostname= False
ctx.verify_mode= ssl.CERT_NONE

#defining api key and parameter
key= 'wIsdMkfbmY3FVVROQ2qc'
para=dict()
para["apikey"]=key

#asking for time and stop number from the user
time=input("What period of time do you want to search for?")
StopNo= input("which bus stop are you looking for?")
para["TimeFrame"]= int(time)
service_url='https://api.translink.ca/rttiapi/v1/stops/'

#defining the url and defining the content type
url= service_url + StopNo + "/" + "estimates?" +urllib.parse.urlencode(para) 
req=Request(url)
req.add_header('Content-Type','application/JSON')
data= urlopen(req,context=ctx).read()

#organize the data 
js= json.loads(data)
dump=json.dumps(js,indent=4)
print(dump)
destination= js[0]["Schedules"][0]["Destination"]
i=0
p=0
print(len(js))
while p < len(js):
    p+1
    while i<len(js[p-1]["Schedules"]):
        destination= js[p-1]["Schedules"][0]["Destination"]
        print("The", js[p-1]["RouteNo"], "to", destination ,  'is at' , js[p-1]["Schedules"][i]["ExpectedLeaveTime"])
        i= i + 1


# 

# In[ ]:





# In[ ]:




