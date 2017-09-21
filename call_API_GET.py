import httplib
conn = httplib.HTTPSConnection("us.wio.seeed.io", 443)
conn.request("GET", "/v1/node/GroveMoistureA0/moisture?access_token=6b186b35b03cf3f1f17b9c09b93c094b")
r1 = conn.getresponse()
print r1.status, r1.reason
data1 = r1.read()
print data1
conn.close()