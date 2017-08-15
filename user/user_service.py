import random
import  json
import hashlib
import http.client
from .user_model import User
from trip.trip_service import Trip_Service
from url_config import WX
from .json_to_dict import JsonObject
from wx.wxdatacrypt import WXBizDataCrypt

class User_Service:

    def __init__(self):
        pass

    @classmethod
    def get_user_by_openid(cls,openid):
        user=User.objects(openid=openid)
        return user

    @classmethod
    def insert_new_user(cls,openid,userinfo):
        user=cls.get_user_by_openid(openid).first()
        if user:
            return user.sessionid
        else:
            h=hashlib.new('ripemd160')
            h.update(openid.encode('utf-8'))
            sessionid=h.hexdigest()
            new_user=User()
            new_user.openid=openid
            new_user.sessionid=sessionid
            new_user.avatar_l=str(userinfo.avatarUrl)
            new_user.country=str(userinfo.country)
            new_user.province=str(userinfo.province)
            new_user.city=str(userinfo.city)
            new_user.gender=userinfo.gender
            new_user.name=str(userinfo.nickName)
            new_user.save()
            return sessionid

    @classmethod
    def get_user_by_id(cls,userid): 
        data=User.objects(id=userid).first() 
        user=data.user_to_dict
        trips=Trip_Service.get_trips_by_userid(userid)
        return {"user":user,"trips":trips}

    @classmethod
    def get_user_session_key(cls,param):
        conn=http.client.HTTPSConnection(WX['host'])
        url=WX['url'] %(WX['appid'],WX['secret'],param.code )
        conn.request('GET',url)
        res=conn.getresponse()
        data=res.read()
        json_data=json.loads(data.decode("utf-8"), object_hook=JsonObject)
        pc = WXBizDataCrypt(WX['appid'], json_data.session_key)
        user_info=pc.decrypt(param.encryptedData, param.iv)
        sessionid=cls.insert_new_user(str(user_info['openId']),param.userInfo)
        return sessionid
