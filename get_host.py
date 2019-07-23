# -*- coding: UTF-8 -*-
# author: YuWei
# time: 2018-06-20

from __future__ import with_statement
from fabric.api import local,settings,abort
from fabric.contrib.console import confirm

def test():
    with settings(warn_only=True):
        result = local('python test.py', capture=True)
        #print result
    if result.failed and not confirm('Test failed. Continue anyway?', default=False):
        abort('test.py is error')