import mysql.connector


class dbutil:
    def init(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="root")
        cur = con.cursor()
        try:
            cur.execute("create database if not exists pydemocrud")
            cur.execute("use pydemocrud")
            cur.execute("create table if not exists pycrud(id int,name varchar(50),emial varchar(30))")
            print("Initialization is done")
        except:
            con.rollback()
        cur.close()
        con.close()

    def insert(self, tpl):
        con = mysql.connector.connect(host="localhost", user="root", passwd="root")
        cur = con.cursor()
        try:
            cur.execute("use pydemocrud")
            st = "insert into pycrud values(%s,%s,%s)"
            cur.execute(st, tpl)
            con.commit()
            print("insertion is successful")
        except:
            con.rollback()
        cur.close()
        con.close()

    def read(self):
        con = mysql.connector.connect(host="localhost", user="root", passwd="root")
        cur = con.cursor()
        try:
            cur.execute("use pydemocrud")
            cur.execute("select * from pycrud")
            res = cur.fetchall()
            if (len(res) == 0):
                print("No data Found")
            else:
                for i in res:
                    print(i)
        except:
            con.rollback()
        cur.close()
        con.close()

    def delete(self, key):
        con = mysql.connector.connect(host="localhost", user="root", passwd="root")
        cur = con.cursor()
        try:
            cur.execute("use pydemocrud")
            cur.execute("delete from pycrud where id=" + str(key))
            con.commit()
            print("deletion is successful")
        except:
            con.rollback()
        cur.close()
        con.close()

    def update(self, id, col, new):
        con = mysql.connector.connect(host="localhost", user="root", passwd="root")
        cur = con.cursor()
        try:
            cur.execute("use pydemocrud")
            cur.execute("update pycrud set " + col + " ='" + str(new) + "' where  id=" + str(id))
            con.commit()
            print("updation is successful")
        except:
            con.rollback()
        cur.close()
        con.close()
