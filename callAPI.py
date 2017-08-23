import httplib, urllib
params = urllib.urlencode({'name': "archer"})
headers = {"Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/plain"}
conn = httplib.HTTPConnection("dd010c2a.ngrok.io:80")
conn.request("POST", "/api/v1.0/print", params, headers)
response = conn.getresponse()
print response.status, response.reason
print response.read()
conn.close()