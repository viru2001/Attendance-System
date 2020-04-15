
import pymysql
myconn = pymysql.connect(host='localhost',user='root',password='password',db='attendance')
print("connection done")

def drop(table_name1):
    sql="drop table "+table_name1
    #print(sql)
    try:
        cur=myconn.cursor()
        cur.execute(sql)
        print("table droppped")
    finally:
            pass#      myconn.close()


def create(table_name):
    try:
        #print("table_name: ", table_name)
        cursor=myconn.cursor()
        #print("table_name: ",table_name)
        #sql="create table "+table_name+"(name varchar(20),d1 int ,d2 int ,d3 int ,d4 int ,d5 int ,d6 int ,d7 int ,d8 int ,d9 int ,d10 int ,d11 int ,d12 int ,d13 int ,d14 int ,d15 int ,d16 int ,d17 int ,d18 int ,d19 int ,d20 int ,d21 int ,d22 int ,d23 int ,d24 int ,d25 int ,d26 int ,d27 int ,d28 int ,d29 int ,d30 int ,d31 int,total double)"
        sql = "create table " + table_name + " (name varchar(50),d1 varchar(5) ,d2 varchar(5) ,d3 varchar(5) ,d4 varchar(5) ,d5 varchar(5) ,d6 varchar(5) ,d7 varchar(5) ,d8 varchar(5) ,d9 varchar(5) ,d10 varchar(5) ,d11 varchar(5) ,d12 varchar(5) ,d13 varchar(5) ,d14 varchar(5) ,d15 varchar(5) ,d16 varchar(5) ,d17 varchar(5) ,d18 varchar(5) ,d19 varchar(5) ,d20 varchar(5) ,d21 varchar(5) ,d22 varchar(5) ,d23 varchar(5) ,d24 varchar(5) ,d25 varchar(5) ,d26 varchar(5) ,d27 varchar(5) ,d28 varchar(5) ,d29 varchar(5) ,d30 varchar(5) ,d31 varchar(5),total varchar(10))"
        #sql="create table student(name varchar(20),d1 int ,d2 int ,d3 int ,d4 int ,d5 int ,d6 int ,d7 int ,d8 int ,d9 int ,d10 int ,d11 int ,d12 int ,d13 int ,d14 int ,d15 int ,d16 int ,d17 int ,d18 int ,d19 int ,d20 int ,d21 int ,d22 int ,d23 int ,d24 int ,d25 int ,d26 int ,d27 int ,d28 int ,d29 int ,d30 int ,d31 int,total double)"
        cursor.execute(sql)
        print("table created")
    finally:
        cursor.close()

def insert1(args,tableName) :

    try :
        cursor = myconn.cursor()
        args = tuple(args)
        #cursor = myconn.cursor()
        #print(tableName)
        sql="insert into " +tableName+ " values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"

        #print(args)
        cursor.execute(sql % args)
        myconn.commit()
       # print(i+1," inserted")
    except Exception:
        pass
        #print("problem")
    finally:
        pass
         #print("Jai Mata di")
'''def insert1(args) :

    try :
        cursor = myconn.cursor()
        for i in range(74):
            for k in range(33)
            #cursor = myconn.cursor()
            sql="insert into student values('%s','%s','%s')"
            args=(i+1,list[i],total[i])
            print(args)
            cursor.execute(sql % args)
            myconn.commit()
            print(i+1," inserted")
    finally:
        cursor.close()
        myconn.close()'''
#drop()
#create()
#insert1()