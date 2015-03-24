import os
import MySQLdb

env = os.getenv('SERVER_SOFTWARE')
if env and env.startswith('Google App Engine/') or os.getenv('SETTINGS_MODE') == 'prod':
    # Connecting from App Engine
    db = MySQLdb.connect(
        unix_socket='/cloudsql/test-authentic:auth-test-cloudsql-instance',
        db='userena_db',
        user='root',
    )
else:
    # Connecting to localhost
    db = MySQLdb.connect(host='127.0.0.1', port=3306, db='userena_db', user='root', passwd='password')

delete_str = 'DELETE FROM django_site WHERE id in (2, 3, 4);'
insert_str = 'INSERT INTO django_site (id, domain, name) VALUES (%s, %s, %s), (%s, %s, %s), (%s, %s, %s);'
insert_tuple = ('2', 'localhost:8000', 'localhost:8000')
insert_tuple += ('3', 'localhost:8080', 'localhost:8080')
insert_tuple += ('4', 'test-authentic.appspot.com', 'test-authentic.appspot.com')

cursor = db.cursor()
cursor.execute(delete_str)
cursor.execute(insert_str, insert_tuple)
db.commit()