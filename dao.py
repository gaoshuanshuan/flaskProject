from flask_sqlalchemy import SQLAlchemy, BaseQuery

db = SQLAlchemy()
def init_db(app):
    db.init_app(app)

def query(cls) -> BaseQuery:
    return db.session.query(cls)

def queryAll(cls): #查询所有
    return query(cls).all()

def queryById(cls,id): #根据id查找数据
    return query(cls).get(int(id))

def add(obj): #添加
    db.session.add(obj)
    db.session.commit()

def delete(obj): #删除
    db.session.delete(obj)
    db.session.commit()
def deleteById(cls,id):
    try:
        obj = queryById(cls,id)
        delete(obj)
        return True
    except:
        pass
    return False