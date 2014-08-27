#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'XingKaiXin.me'


import mysql.connector


conn = mysql.connector.connect(user='root',  database='test', use_unicode=True)

cursor = conn.cursor()

#cursor.execute("create table user(id varchar(20), name varchar(20))")

#cursor.execute("insert into user values(%s,%s)", ["1", "Kevin"])

cursor.execute("select * from user where id = %s", "1")
values = cursor.fetchall()
print values

print cursor.rowcount


conn.commit()
cursor.close()