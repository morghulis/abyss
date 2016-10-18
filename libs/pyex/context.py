# -*- coding:utf-8 -*-

class ContextDocker(object):

    def __init__(self, **kwargs):
        self.__dict__['default_kvs'] = kwargs
        self.reset(**kwargs)


    def docker(self, method):
        def wrapper(*args, **kwargs):
            return method(*args, **kwargs)
        return wrapper


    def reset(self, **kwargs):
        if kwargs == {}:
            kwargs = self.__dict__['default_kvs']

        self.__dict__['ctxvars'] = {}
        for k in kwargs.keys():
            self.__dict__['ctxvars'][k] = kwargs[k]


    def __setattr__(self, name, value):
        self.__dict__['ctxvars'][name] = value


    def __getattr__(self, name):
        return self.__dict__['ctxvars'].get(name)
