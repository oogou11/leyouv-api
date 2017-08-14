import base64
import datetime
import  json
import random
import hashlib
import http.client
from http import cookies
from .user_model import User
from trip.trip_service import Trip_Service
from .session_model import Session
from url_config import WX
from .json_to_dict import JsonObject
from wx.wxdatacrypt import WXBizDataCrypt

class User_Service:

    def __init__(self):
        pass
    
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
         user_info['nickName'].decode("base64")
         return "succ"
