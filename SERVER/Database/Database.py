import pymysql, time

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
            # 提交到数据库执行
            self.db.commit()
            # 结果
            results = self.cursor.fetchall()
            return results
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

    def showdata(self, tablename):
        sql = f"select * from {tablename}"
        results = self.execute(sql)
        return results
    
    # item: [("username", "char(20)")]
    def createtable(self, tablename, item):
        sql = f"create table {tablename} ("
        for i in item:
            sql += " ".join(i)
            if item.index(i) != len(item) - 1:
                sql += ", "
            else:
                sql += ")"
        results = self.execute(sql)
        return results

    def deletetable(self, tablename):
        sql = f"drop table {tablename}"
        res = self.execute(sql)
        return res

    def deleteitem(self, ID, tablename = "knowledgeitem"):
        sql = f"delete from {tablename} where ID = {ID};"
        results = self.execute(sql)
        return results

    def insertdata(self, tablename, values):
        # SQL 插入语句
        try:
            if tablename == "userinfo":
                sql = f"INSERT INTO userinfo (username, UUID, password, registertime, bio, permission) VALUES {values[0], values[1], values[2], values[3], values[4], values[5]}"
            elif tablename[0:4:1] == "room0":
                sql = f"INSERT INTO room0 (username, msgcontent, msgtime, msgtype) VALUES {values[0], values[1], values[2], values[3]}"
            results = self.execute(sql)
            return results
        except Exception as e:
            # 如果发生错误则回滚
            print("error  ", e)

    def user_exist(self, permission: int, username: str, password: str):
        sql = f"SELECT * FROM userinfo WHERE permission = 1 and username = \"{username}\" and password = \"{password}\";"
        results = self.execute(sql)
        print(sql)
        return results

    def close(self):
        # 关闭数据库连接
        self.db.close()

if __name__ == "__main__":
    DB = DBConnecter()
    # values = ["Sakura", "16666666", "test", "2020", "hihi", "1"]
    # DB.insertdata("userinfo", values)
    # res = DB.showdata("userinfo")
    # print(res)
    DB.close()