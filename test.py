#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# OrderedDict 实现队列

# from collections import OrderedDict
#
# class LastUpdatedOrderedDict(OrderedDict):
#
#     def __init__(self, capacity):
#         super(LastUpdatedOrderedDict, self).__init__()
#         self._capacity = capacity
#
#     def __setitem__(self, key, value):
#         containsKey = 1 if key in self else 0
#         print self, key, containsKey
#         if len(self) - containsKey >= self._capacity:
#             last = self.popitem(last=False)
#             print 'remove:', last
#         if containsKey:
#             del self[key]
#             print 'set:', (key, value)
#         else:
#             print 'add:', (key, value)
#         OrderedDict.__setitem__(self, key, value)
#
#
# capacity=3
# #aa=OrderedDict([('a',1),('b',2),('c',3)])
# cc=LastUpdatedOrderedDict(capacity)
# cc['a']=1
# cc['b']=2
# cc['c']=3
# cc['d']=4
# cc['d']=5
# print cc


# import MySQLdb
#
# def connectdb():
#     print '连接到mysql服务器...'
#     db=MySQLdb.connect(user='root',passwd='yuwei',host='localhost',db='test')
#     print '已连接%s' % db
#     return db
#
# def createtable(db):
#     # 使用cursor()方法获取操作游标
#     cursor=db.cursor()
#
#     # 如果存在表Sutudent先删除
#     cursor.execute("DROP TABLE IF EXISTS Student")
#     sql=""" create table Student (
#     id INT(10) NOT NULL ,
#     name VARCHAR(20),
#     grade INT )"""
#
#     cursor.execute(sql)
#
# def insertdb(db):
#     cursor = db.cursor()
#
#     #sql插入语句
#     sql = """ insert into Student VALUES ('001','CKY',90),
#                                          ('002','YW',95),
#                                          ('003','YQ',100),
#                                          ('004','CDM',85)
#                                          """
#
#     try:
#         cursor.execute(sql)
#         # 提交到数据库执行
#         db.commit()
#     except:
#         print '插入数据失败!'
#         db.rollback()
#
# def updatedb(db):
#     cursor=db.cursor()
#
#     sql=""" update Student set name='BaoBao' where id='1' """
#
#     try:
#         cursor.execute(sql)
#         db.commit()
#     except:
#         print "更新数据失败!"
#         db.rollback()
#
# def querydb(db):
#     cursor=db.cursor()
#
#     sql=""" select * from Student """
#     try:
#         cursor.execute(sql)
#         #获取所有记录列表
#         result=cursor.fetchall()
#         # print result
#         for row in result:
#             Id = row[0]
#             Name = row[1]
#             Grade = row[2]
#             print "%s,%s,%s" % (Id,Name,Grade)
#     except:
#         print 'Error:unable to fecth data'
#
# def deletedb(db):
#     cursor=db.cursor()
#
#     sql=''' delete from Student where id="4" '''
#
#     try:
#         cursor.execute(sql)
#         db.commit()
#     except Exception, e:
#         print "删除失败!"
#         print e
#         db.rollback()
#
# def closedb(db):
#     db.close()
#     print '数据库断开连接'
#
# def main():
#     db=connectdb()
#
#     createtable(db)
#     insertdb(db)
#     #updatedb(db)
#     deletedb(db)
#     querydb(db)
#     closedb(db)
#
# if __name__ == '__main__':
# #     main()
#
# from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, MetaData, ForeignKey
#
#
# def createDB(engine):
#     # 获取元数据
#     metadata = MetaData()
#     # 定义表
#     user = Table('user', metadata,
#                  Column('id', Integer, primary_key=True),
#                  Column('name', String(30)),
#                  Column('score', Integer)
#                  )
#
#     color = Table('color', metadata,
#                   Column('id', Integer, primary_key=True),
#                   Column('name', String(20)),
#                   )
#
#     metadata.create_all(engine)
#
#
# def InsertDB(engine):
#     sql = """insert into test.user(id,name,score) VALUES ('1','chenkeyu','90');"""
#     engine.execute(sql)
#
#
# def ShowDB(engine):
#     sql = """ select * from user; """
#     result = engine.execute(sql)
#     print result
#
#
# def updateDB():
#     pass
#
#
# def main():
#     # 创建数据库连接
#     engine = create_engine("mysql+mysqldb://root:yuwei@localhost:3306/test")
#     # createDB(engine)
#     # InsertDB(engine)
#     ShowDB(engine)
#
#
# if __name__ == '__main__':
#     main()

# import json
#
#
# class Gifts(object):
#     def __init__(self):
#         self.gift_list = ['口红', '包包', '防晒霜']
#         self.used_list = []
#
#     def get_gift(self):
#         gift_list = json.dumps(self.gift_list, encoding='utf-8', ensure_ascii=False)
#         gift = raw_input('请选择您要使用的物品%s:' % gift_list)
#         if gift in self.gift_list:
#             return gift
#         else:
#             print "物品不存在!"
#             exit(1)
#
#     def __call__(self, *args, **kwargs):
#         gift = self.get_gift()
#         while gift:
#             if gift in self.used_list:
#                 print "%s已使用!" % gift
#             else:
#                 self.used_list.append(gift)
#                 print '您正在使用%s' % gift
#
#             # 判断物品是否都已使用
#             if len(self.used_list) == len(self.gift_list):
#                 print "物品都已使用!"
#                 exit()
#
#             a = raw_input('是否继续使用其他物品(y/n):')
#             if a.lower() == 'y':
#                 gift = self.get_gift()
#             else:
#                 exit(0)
#
#
# if __name__ == '__main__':
#     p = Gifts()
#     p.__call__()


def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
