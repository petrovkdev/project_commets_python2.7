#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as db
import sys

# Подключаемся к базе данных
con = db.connect('testdb.db')
con.text_factory = str
cur = con.cursor()

# Создание таблицы комментариев
cur.execute("CREATE TABLE comments(id INTEGER PRIMARY KEY, first_name VARCHAR(100), name VARCHAR(100), last_name VARCHAR(100), region INTEGER, city INTEGER, phone VARCHAR(100), email VARCHAR(100), comment TEXT, timestamp DATETIME INTEGER)")

cur.execute("CREATE TABLE regions(id INTEGER PRIMARY KEY, region VARCHAR(100))")

cur.execute("CREATE TABLE city(id INTEGER PRIMARY KEY, city VARCHAR(100), region_id INTEGER)")

# Вставка предварительных данных в таблицы regions и city
cur.execute("INSERT INTO regions VALUES(1, 'Краснодарский край')")
cur.execute("INSERT INTO regions VALUES(2, 'Ростовская область')")
cur.execute("INSERT INTO regions VALUES(3, 'Ставропольский край')")

cur.execute("INSERT INTO city VALUES(1, 'Краснодар', 1)")
cur.execute("INSERT INTO city VALUES(2, 'Кропоткин', 1)")
cur.execute("INSERT INTO city VALUES(3, 'Славянск', 1)")
cur.execute("INSERT INTO city VALUES(4, 'Ростов', 2)")
cur.execute("INSERT INTO city VALUES(5, 'Шахты', 2)")
cur.execute("INSERT INTO city VALUES(6, 'Батайск', 2)")
cur.execute("INSERT INTO city VALUES(7, 'Ставрополь', 3)")
cur.execute("INSERT INTO city VALUES(8, 'Пятигорск', 3)")
cur.execute("INSERT INTO city VALUES(9, 'Кисловодск', 3)")

con.commit()
con.close() 