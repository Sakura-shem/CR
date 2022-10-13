import pymysql, uuid

class DBConnecter():
    def __init__(self, user, password, database):
        self.user = user
        self.password = password
        self.database = database
        # 打开数据库连接
        self.db = pymysql.connect(host='localhost', user = user, password = password, database = database)
        
        # 使用 cursor() 方法创建一个游标对象 cursor
        self.cursor = self.db.cursor()

    def execute(self, sql):
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            desc = self.cursor.description
            # 提交到数据库执行
            self.db.commit()
            # 结果
            results = self.cursor.fetchall()
            return results, desc
        except Exception as e:
            return e

    def ping(self):
        try:
            self.db.ping()
            print("ok")
        except:
            self.db = pymysql.connect(host='localhost', user = self.user, password = self.password, database = self.database)
            self.cursor = self.db.cursor()
            print("error")

    # item: [("username", "char(20)")]
    def createtable(self, tablename, item):
        try:
            sql = f"create table {tablename} ("
            for i in item:
                sql += " ".join(i)
                if item.index(i) != len(item) - 1:
                    sql += ", "
                else:
                    sql += ")"
            res, desc = self.execute(sql)
        except Exception as e:
            res = "error"
            print("error  ", e)
        return res

    def showalltable(self, show = True):
        sql = "show tables;"
        res, desc = self.execute(sql)
        tables = [i[0] for i in res]
        if show:
            print(tables)
        return tables

    def showtabledata(self, tablename):
        sql = f"select * from {tablename}"
        res, desc = self.execute(sql)
        print(res)
        return res

    def getfield(self, tablename):
        sql = f"select * from {tablename}"
        res, desc = self.execute(sql)
        field = [i[0] for i in desc]
        # for i in desc:
        #     print(i)
        return field

    def getfielddata(self, tablename, fieldname):
        sql = f"select {fieldname} from {tablename}"
        res, desc =  self.execute(sql)
        return res
    
    def insertstrdata(self, tablename, values):
        try:
            field = self.getfield(tablename)
            sql = f"INSERT INTO {tablename} (" + ", ".join(field) + ") VALUES ('" + "', '".join(values) + "');"
            res, desc = self.execute(sql)
            return res
        except Exception as e:
            res = "error"
            print("error  ", e)
        return res

    def cleartable(self, tablename):
        sql = f"truncate table {tablename}"
        res, desc = self.execute(sql)
        return res

    def deletetable(self, tablename):
        sql = f"drop table {tablename}"
        res, desc = self.execute(sql)
        return res

    def deletealltables(self):
        try:
            tables = self.showalltable(show = False)
            for i in tables:
                res = self.deletetable(i)
        except Exception as e:
            res = "error"
            print("error  ", e)
        return res

    def close(self):
        # 关闭数据库连接
        self.db.close()
    
    def adduser(self, values):
        res = self.insertstrdata("user", values)
        return res

    def addroom(self, values):
        # insert item to room table 
        res = self.insertstrdata("room", values)
        # create new table roomid
        self.createroom(values[0])
        return res
    
    def createroom(self, roomid):
        try:
            res = self.createtable(roomid, [("username", "char(20)"), ("msgcontent","TEXT"), ("msgtime", "char(20)"), ("msgtype", "char(20)")])
        except Exception as e:
            res = "error"
            print("error  ", e)
        return res

    def roomlist(self):
        res = self.getfielddata("room", "roomname")
        print(res)

    def roominfo(self):
        res = self.showtabledata("room")
        return res

    def deleteroom(self, roomid: str):
        try:
            res, desc = self.deletetable(roomid)
        except Exception as e:
            res = "error"
            print("error  ", e)
        return res

    def addroommsg(self, roomid, ):
        self.insertdata(roomid)

def init():
    DB = DBConnecter("root", "DB666SHEM", "CR")
    # clear all table
    DB.deletealltables()

    # create basic table
    DB.createtable("user", [("username", "char(32)"), ("UUID", "char(32)"), ("password", "char(32)"), ("registertime", "char(32)"), ("portrait", "char(32)"), ("bio", "char(32)"), ("permission", "char(32)")])
    DB.createtable("room", [("roomid", "char(32)"), ("roomname", "char(32)"), ("roombio", "char(32)"), ("roomlogo", "char(32)"), ("createtime", "char(32)"), ("roomtype", "char(32)")])
    
    # add info to basic table
    userid = str(int(uuid.uuid4()))[0:16:1]
    DB.adduser(["testuser", userid, "first666", "2020.10.13-21:36", userid + ".jpg" ,"test", "0"])
    DB.addroom(["room" + str(int(uuid.uuid4()))[0:6:1], "testroom0", "test basic functions", "testroom0.jpg", "2020.10.13-21:36", "test"])
    DB.addroom(["room" + str(int(uuid.uuid4()))[0:6:1], "testroom1", "test advanced functions", "testroom1.jpg", "2020.10.13-21:36", "test"])
    
    tables = DB.showalltable()
    DB.roominfo()
    DB.close()

if __name__ == "__main__":
    init()



    # CREATE USER TABLE
    # DB.createtable("user", [("username", "char(32)"), ("UUID", "char(32)"), ("password", "char(32)"), ("registertime", "char(32)"), ("bio", "char(32)"), ("permission", "char(32)")])
    # CREATE ROOMLIST TABLE
    # DB.createtable("room", [("roomid", "char(32)"), ("roomname", "char(32)"), ("roombio", "char(32)"), ("roomlogo", "char(32)"), ("createtime", "char(32)"), ("roomtype", "char(32)")])
    # res = DB.adduser(["testuser", str(int(uuid.uuid4()))[0:16:1], "first666", "2020.10.13-21:36", "test", "0"])
    # res = DB.addroom([ "room" + str(int(uuid.uuid4()))[0:6:1], "testroom0", "test basic functions", "testroom0.jpg", "2020.10.13-21:36", "test"])
    # res = DB.addroom([ "room" + str(int(uuid.uuid4()))[0:6:1], "testroom1", "test advanced functions", "testroom1.jpg", "2020.10.13-21:36", "test"])
    