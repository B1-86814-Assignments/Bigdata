from pyhive import hive

# hive config
host_name = 'localhost'
port = 10000
user = 'sunbeam'
password = ' '
db_name = 'edbda'

# get hive connection
conn = hive.Connection(host=host_name, port=port, username=user, password=password, database=db_name, auth='CUSTOM')

# get the cursor object
cur = conn.cursor()

# execute the sql query using cursor
mid = int(input('Enter movie id: '))
sql = """
WITH movie_recom AS (
SELECT 
IF(m1= %s, m2, m1) movieid 
FROM corr_movies c 
WHERE cor > 0.6 AND cnt > 10 AND (m1 = %s or m2 = %s))
SELECT mr.movieid, ms.title 
FROM movie_recom mr 
INNER JOIN movie_staging ms ON mr.movieid = ms.movieid
"""

cur.execute(sql, [mid, mid, mid])

# collect/process result
result = cur.fetchall()
for row in result:
    print(row)

# close the connection
conn.close()