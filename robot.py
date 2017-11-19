#!/usr/bin/env python

"""
Some notes:

- robot params are POSTed in HTTP headers

"""

import json
import requests
import numpy as np


class Printable(object):
    def __str__(self):
        """ Readable print of object name and properties - str(o)
        """
        lines = [self.__class__.__name__]
        for field, value in self.__dict__.items():
            lines.append("  " + field + " = " + repr(value))
        return '\n'.join(lines)
    def to_json(self):
        """ Get object properties as indented json """
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)


class Pose(Printable):
    def __init__(self, angles):
        self.angles = angles


class Position(Printable):
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
            r = requests.post(self.url + path)
        else:
            r = requests.post(self.url + path, headers=headers)
        print(r.status_code)

    def _get(self, path):
        r = requests.get(self.url + path)
        print(r.status_code)
        return r.json()

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
        res = self._get('/getPosition')
        p = res['point']
        r = res['rotation']
        return Position(p['x'], p['y'], p['z'], r['roll'], r['pitch'], r['yaw'])

    def getPose(self):
        # {'angles': [-0.0089, 90.0, 0.0027, -89.9973, 89.9987, 0.0013]}
        r = requests.get(self.url + '/getPose')
        print(r.status_code)
        res = r.json()
        return Pose(res['angles'])

    def setPose(self, pose):
        if isinstance(pose, Pose):
            headers = {'angles': str(pose.angles)}
        else:
            headers = {'angles': str(pose)}
        # angles: [0.0007, 89.998, 0.002, -89.998, 89.9987, 0.002]
        # angles: [10.0007, 89.998, 0.002, -89.998, 89.9987, 0.002]
        self._post('/setPose', headers=headers)

    # numpy

    def getPositionMatrix(self):
        res = self._get('/getPositionMatrix')
        return np.array(
            [
                [res[u'a11'], res[u'a12'], res[u'a13'], res[u'a14']],
                [res[u'a21'], res[u'a22'], res[u'a23'], res[u'a24']],
                [res[u'a31'], res[u'a32'], res[u'a33'], res[u'a34']],
                [res[u'a41'], res[u'a42'], res[u'a43'], res[u'a44']]
            ])

    def gotoPosition(self, point, rotation):
        pass

    def gotoPositionNoAngle(self, point):
        pass


if __name__ == '__main__':
    r = Robot('http://100.95.255.181:8080')

    pos = r.getPosition()
    print(pos)

