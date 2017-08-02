from flask import jsonify

class APIResult(dict):
    def __init__(self, code, result=None, msg=None):
        self["code"] = code
        self["msg"] = msg
        if result is None:
            result = {}
        self["result"] = result

    def jsonify(self):
        return jsonify(**self)

    def __call__(self, *arg, **kw):
        return self.jsonify()

class api_wrap(object):
    def __init__(self, func):
        super(api_wrap, self).__init__()
        self._func = func
        self.__name__ = func.__name__

    def __get__(self, instance, owner):
        def wrap(*arg, **kw):
            return self._func(instance, *arg, **kw)

        wrap.__name__ = self._func.__name__
        return wrap

    def __call__(self, *arg, **kw):
        res = self._func(*arg, **kw)
        if isinstance(res, APIResult):
            return res.jsonify()
        return res