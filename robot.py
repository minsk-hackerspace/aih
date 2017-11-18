#!/usr/bin/env python

import json
import requests
import numpy as np



class Position:
    def __init__(self, x, y, z, roll, pitch, yaw):
        self.x = x
        self.y = y
        self.z = z
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw


class Robot:
    def __init__(self, url):
        self.url = url
        self.decoder = json.JSONDecoder()
        self.encoder = json.JSONEncoder()

    def _get_json(self, command):
        r = requests.get(self.url + '/' + command)
        return r.json()

    def _request_json(self, command, data):
        data = json.dumps(data)
        req = urllib2.Request(self.url + '/' + command, data, {'Content-Type': 'application/json'})
        f = urllib2.urlopen(req)
        response = f.read()
        f.close()
        print response
        return self.decoder.decode(response)

    def gotoPosition(self, point, rotation):
        data = {}
        self._request_json('gotoPosition', data)
        pass

    def gotoPositionNoAngle(self, point):
        pass

    def grip(self, force):
        pass

    def getPosition(self):
        r = requests.get(self.url + '/getPosition')
        res = r.json()
        print res
        return Position(res[u'point'][u'x'], res[u'point'][u'y'], res[u'point'][u'z'], res[u'rotation'][u'roll'], res[u'rotation'][u'pitch'], res[u'rotation'][u'yaw'])

    def getPositionMatrix(self):
        res = self._get_json('getPositionMatrix')
        return np.array(
            [
                [res[u'a11'], res[u'a12'], res[u'a13'], res[u'a14']],
                [res[u'a21'], res[u'a22'], res[u'a23'], res[u'a24']],
                [res[u'a31'], res[u'a32'], res[u'a33'], res[u'a34']],
                [res[u'a41'], res[u'a42'], res[u'a43'], res[u'a44']]
            ])


r = Robot('http://100.95.255.181:8080')

pos = r.getPosition()
print(pos)
