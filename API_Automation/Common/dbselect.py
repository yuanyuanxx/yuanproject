# -*- coding:utf-8 -*-
#from API_Automation.database import dbinformation as dbin

def select_user(db):
    cur = db.cursor()
    cur.execute('select * from users')
    values = cur.fetchall()  # 获取结果集中的所有行
    return values

