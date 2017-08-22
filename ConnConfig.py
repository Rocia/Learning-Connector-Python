#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 13:15:44 2017

@author: root
"""

import mysql.connector

config = {
  'user': 'root',
  'password': 'root@123',
  'host': '127.0.0.1',
  'database': 'citation',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)

cnx.close()