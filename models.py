#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   models.py
@Time    :   2021/08/13 15:03:44
@Author  :   JayZhang 
@Version :   1.0
@Contact :   597952291@qq.com
@License :   (C)Copyright 2021, iceiceice
@Desc    :   None
'''

# here put the import lib
import time
from sqlalchemy import CHAR, Float, Column, DateTime, ForeignKey, Index, JSON, String, Text, Table, Time, BOOLEAN
from sqlalchemy.dialects.mysql import BIGINT, INTEGER
from sqlalchemy.ext.declarative import declarative_base


# here put the main code
Base = declarative_base()
metadata = Base.metadata


class Answers(Base):
    """Answers表"""
    __tablename__ = 'answers'

    id = Column(BIGINT(20), primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False)
    mobile = Column(String(32), nullable=False)
    gender = Column(BOOLEAN, nullable=False)
    theme = Column(INTEGER(11), nullable=False)
    score = Column(INTEGER(11), nullable=False)
    createat = Column(BIGINT(20), nullable=False, default=time.time()*100000)
    updateat = Column(BIGINT(20))
    removeat = Column(BIGINT(20))
