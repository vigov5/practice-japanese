import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql://ja_admin:ja_admin@localhost/ja_db'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLED = True
SECRET_KEY = '&*(PSDSAD:H#*&!kllhui!@*&!0!#+pj;!@-12'
