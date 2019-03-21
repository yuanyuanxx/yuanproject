import requests
import json
def checkGetSubject(url,params):
    r = requests.get(url,params)
    print(r.url)
    jsonresult=r.json()
    print(json.dumps(jsonresult,indent=2))
    #检查接口返回的关键词是否正确
    keys=['subjects','total']
    foundimportantkeys=[k for k in keys if k in jsonresult]
    print(foundimportantkeys)
    assert len(foundimportantkeys)==2
    if r.status_code==200:
        return True
    elif r.status_code=='345':
        return False
        print("接口返回错误")
