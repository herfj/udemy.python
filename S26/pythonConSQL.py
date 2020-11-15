import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='pytest'
)

cursor=db.cursor()
cursor2=db.cursor()

# SELECTS

# cursor.execute('select * from estudiante')
# res = cursor.fetchall()
# print(res)
# print()
# print()
# print()
# cursor2.execute('select * from estudiante')
# res2 = cursor2.fetchone()
# print(res2)


#INSERTS


# cursor.execute('show create table user')

# sql = 'insert into user value (%s, %s, %s,%s)'
# values = (2,'tomas','baute', 19)

# cursor2.execute(sql, values)

# db.commit()

# print(cursor.rowcount)


#UPDATE


# sql = 'update user set edad=%s where id=%s'
# values = (16, 2)

# cursor2.execute(sql, values)

# db.commit()


#DELETE

sql = 'delete from user where id=%s'
values = (2,)
cursor.execute(sql, values)
db.commit()