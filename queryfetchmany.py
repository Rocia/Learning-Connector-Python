#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 16:45:21 2017

@author: root
"""
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def iter_row(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row

	
	