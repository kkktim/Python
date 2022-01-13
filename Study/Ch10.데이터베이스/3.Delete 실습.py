import pymysql

conn = pymysql.connect(host='54.180.160.240',
                       user='rkdxogh1987',
                       password='1234',
                       db='rkdxogh1987',
                       charset='utf8')

cur = conn.cursor()

sql = "DELETE FROM `User1` WHERE `uid` = 'P101';"
cur.execute(sql)
conn.commit()

conn.close()

print("Delete 완료...")
