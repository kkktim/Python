import pymysql

# 접속
conn = pymysql.connect(host='54.180.160.240',
                       user='rkdxogh1987',
                       db='rkdxogh1987',
                       password='1234',
                       charset='utf8')

# 객체 생성
cur = conn.cursor()

# SQl 실행
sql = "UPDATE `User1` SET `age` = `age` + 1 WHERE `uid` = 'P101';"
cur.execute(sql)
conn.commit()

# 종료
conn.close()

print('Update 완료...')