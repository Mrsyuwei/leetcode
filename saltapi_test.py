# -*- coding: UTF-8 -*-

import urllib, urllib2, json, re


class saltAPI(object):
    def __init__(self):
        self.__url = "https://192.168.137.130:8002"
        self.__user = 'saltapi'
        self.__password = 'yuwei'
        self.__token_id = self.salt_login()

    def salt_login(self):
        params = {'eauth': 'pam', 'username': self.__user, 'password': self.__password}
        encode = urllib.urlencode(params)
        headers = {'X-Auth-Token': ''}
        url = self.__url + '/login'
        req = urllib2.Request(url, encode, headers)
        opener = urllib2.urlopen(req)
        content = json.loads(opener.read())
        #print content
        try:
            token = content['return'][0]['token']
            return token
        except KeyError:
            raise KeyError

    def postRequest(self, obj, prefix='/'):
        url = self.__url + prefix
        headers = {'X-Auth-Token': self.__token_id}
        req = urllib2.Request(url, obj, headers)
        opener = urllib2.urlopen(req)
        content = json.loads(opener.read())
        # print content['return']
        return content['return']

    def saltCmd(self, params):
        obj = urllib.urlencode(params)
        obj, number = re.subn('arg\d', 'arg', obj)
        res = self.postRequest(obj)
        return res


def main():
    # 以下是用来测试saltAPI类的部分
    sapi = saltAPI()
    params = {'client': 'local', 'fun': 'test.ping', 'tgt': '*'}
    # params = {'client':'local', 'fun':'test.ping', 'tgt':'某台服务器的key'}
    # params = {'client':'local', 'fun':'test.echo', 'tgt':'某台服务器的key', 'arg1':'hello'}
    # params = {'client':'local', 'fun':'test.ping', 'tgt':'某组服务器的组名', 'expr_form':'nodegroup'}
    test = sapi.saltCmd(params)
    print test


if __name__ == '__main__':
    main()
