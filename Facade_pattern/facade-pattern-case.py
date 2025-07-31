import pymysql
import re

class DBHelper:
    __host = "localhost"
    __username ="root"
    __password = "password"
    __database = "test_db"  
    __conn = None
    __cursor = None 

    def __init__(self):
        try:
            self.__conn = pymysql.connect(
                self.__host, self.__username, self.__password, self.__database, charset="utf8")
            self.__cursor = self.__conn.cursor()         
            
        except:
            raise "Database connection failed"
        
    def execute_query(self, sql):
        try:
            self.__cursor.execute(sql)
            records = self.__cursor.fetchall()
            self.commit()
            return records
        except Exception as e:
            print(f"Error executing query: {e}")    
            self.rollback()

    def execute_update(self, sql):
        try:
            self.__cursor.execute(sql)
            self.commit()
            return True
        except Exception as e:
            print(f"Error executing update: {e}")
            self.rollback()
        return False
    
    def commit(self):
        self.__conn.commit()
    
    def rollback(self):
        self.__conn.rollback()
    
    def close(self):
        try:
            if not self.__conn:
                self.__conn.close()
        except e:
            print(f"Error closing connection: {e}")

db = DBHelper()
sql = "insert into book(title, price) values('Python Design Patterns', 99.9)"
db.execute_update(sql)
sql = "update book set price = 80 where id=1"
db.execute_update(sql)

sql = "select * from book"
results = db.execute_query(sql)
for row in results:
    print(f"ID: {row[0]}, Title: {row[1]}, Price: {row[2]}")
db.close()



