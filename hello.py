#!/usr/bin/python
#coding:utf-8

def __private_1(name):
    print 'Hello, %s' % name

def __private_2(name):
    print 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return __private_1(name)
    else:
        return __private_2(name)

greeting('Kelly')
