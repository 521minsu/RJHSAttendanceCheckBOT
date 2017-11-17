#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import sys

try:
    con = _mysql.connect('localhost', 'discordbot', 'M54@5ghbX%97*', 'discord')
        
    con.query("SELECT VERSION()")
    result = con.use_result()
    
    print("MySQL version: %s".format(result))
    
except _mysql.Error, e:
  
    print("Error %d: %s" % (e.args[0], e.args[1]))
    sys.exit(1)

finally:
    
    if con:
        con.close()
