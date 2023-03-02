"""定数モジュール"""
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# データベース接続情報
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')

# Engine の作成
Engine = create_engine(
  "mysql+pymysql://root:@127.0.0.1:3306/alembic_sample",
  encoding="utf-8",
  echo=False
)
Base = declarative_base()
