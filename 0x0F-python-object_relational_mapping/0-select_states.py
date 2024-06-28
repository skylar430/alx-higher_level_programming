#!/usr/bin/python3
""" here you INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada") """
import MySQLdb
import sys 


if _name_ == "_main_":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                        passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c.execute("SELECT * FROM states")
    rows = c.fechall()
    for row in rows:
        print(row)
        c.close()
        db.close()
