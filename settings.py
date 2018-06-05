import os
#设置上传文件的存放位置
BASE_DIR = os.path.dirname(os.path.abspath(__name__))
STATIC_DIR=os.path.join(BASE_DIR,'static')
MEDIA_DIR = os.path.join(STATIC_DIR,'uploads')

class config():
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:root@localhost:3306/user'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #设置session相关参数
    SECRET_KEY='LKJDLJSDKJSDFJDSFLKJSDLFJLSD'
