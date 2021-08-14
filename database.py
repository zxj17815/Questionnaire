#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   database.py
@Time    :   2021/08/13 14:25:14
@Author  :   JayZhang 
@Version :   1.0
@Contact :   597952291@qq.com
@License :   (C)Copyright 2021, iceiceice
@Desc    :   None
'''

# here put the import lib

from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker, Session

from configs.settings import settings

# here put the main code


SQLALCHEMY_DATABASE_URL = settings.DATABASE['questionnaire']

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_recycle=3600, pool_size=0, max_overflow=-1)

SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db_dep():
    """依赖注入-获取数据库连接"""
    db = SessionLocal()
    try:
        # print('获取数据库连接')
        yield db
    finally:
        # print('关闭数据库连接')
        db.close()


def get_db() -> Session:
    """直接获取数据库连接"""
    db = SessionLocal()
    return db