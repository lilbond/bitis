from urllib import request

for t in range(2000, 2010):
    tuid = t
    siteId = 1
    url = "https://api.expedia.com/user/tuid=" + str(tuid) + "?siteid=" + str(siteId)

    response = request.urlopen(url)
    json = response.read()
    print(json)
