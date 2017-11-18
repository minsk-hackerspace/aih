import json
import urllib2
import numpy as np

class Robot:
    def __init__(self,url):
        self.url=url
        self.decoder=json.JSONDecoder()
        self.encoder=json.JSONEncoder()
    
    def _get_json(self,command):
        req = urllib2.Request(self.url+'/'+command)
        f = urllib2.urlopen(req)
        response = f.read()
        f.close()
        return self.decoder.decode(response)
    
    def _request_json(self,command,data):
        data = json.dumps(data)
        req = urllib2.Request(self.url+'/'+command,data, {'Content-Type': 'application/json'})
        f = urllib2.urlopen(req)
        response = f.read()
        f.close()
        print response
        return self.decoder.decode(response)

    def gotoPosition(self,point,rotation):
        data = {}
        self._request_json('gotoPosition',data)
        pass

    def gotoPositionNoAngle(self,point):
        pass

    def grip(self,force):
        pass

    def getPosition(self):
        pass

    def getPositionMatrix(self):
        res=self._get_json('getPositionMatrix')
        return np.array(
                [
                    [res[u'a11'],res[u'a12'],res[u'a13'],res[u'a14']],
                    [res[u'a21'],res[u'a22'],res[u'a23'],res[u'a24']],
                    [res[u'a31'],res[u'a32'],res[u'a33'],res[u'a34']],
                    [res[u'a41'],res[u'a42'],res[u'a43'],res[u'a44']]
                    ])
               
        


