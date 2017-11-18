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

    def _post(self, path, headers=None):
        if headers == None:
            res = requests.post(self.url + path)
        else:
            res = requests.post(self.url + path, headers=headers)
        print(res.status_code)

    def _get_power(self, fast=False):
        if fast:
            return {'power': '40'}
        else:
            return {'power': '5'}

    def openGripper(self, fast=False):
        self._post('/openGripper', headers=self._get_power(fast))

    def closeGripper(self, fast=False):
        self._post('/closeGripper', headers=self._get_power(fast))

    def freeze(self):
        self._post('/freeze')

    def relax(self):
        self._post('/relax')

    def getPosition(self):
        r = requests.get(self.url + '/getPosition')
        res = r.json()
        print res
        return Position(res[u'point'][u'x'], res[u'point'][u'y'], res[u'point'][u'z'], res[u'rotation'][u'roll'], res[u'rotation'][u'pitch'], res[u'rotation'][u'yaw'])


    # --- unstable ---
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

    def getPositionMatrix(self):
        res = self._get_json('getPositionMatrix')
        return np.array(
            [
                [res[u'a11'], res[u'a12'], res[u'a13'], res[u'a14']],
                [res[u'a21'], res[u'a22'], res[u'a23'], res[u'a24']],
                [res[u'a31'], res[u'a32'], res[u'a33'], res[u'a34']],
                [res[u'a41'], res[u'a42'], res[u'a43'], res[u'a44']]
            ])

    def gotoPosition(self, point, rotation):
        data = {}
        self._request_json('gotoPosition', data)
        pass

    def gotoPositionNoAngle(self, point):
        pass


r = Robot('http://100.95.255.181:8080')

pos = r.getPosition()
print(pos)

