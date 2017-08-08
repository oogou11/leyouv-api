
from .user_model import User

class User_Service:

    def __init__(self):
        pass


    @classmethod
    def get_user_by_id(cls,id):
        arr=[]
        data=User.objects(id=id)
        for i in data:
            arr.append(i.user_to_dic)
        return arr