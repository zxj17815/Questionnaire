#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   answers.py
@Time    :   2021/08/13 14:35:55
@Author  :   JayZhang 
@Version :   1.0
@Contact :   597952291@qq.com
@License :   (C)Copyright 2021, iceiceice
@Desc    :   None
'''

# here put the import lib
import datetime
import random
import string
import time

from pydantic import ValidationError
from pydantic.error_wrappers import ErrorWrapper
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from sqlalchemy.sql.functions import func

import models
from schemas import answers as answers_schema


# here put the main code

def list(db: Session, name: str, mobile: str, theme: str, skip: int = 1, limit: int = 10):
    """查询订单列表数据"""
    db_query = db.query(models.Answers)
    if name:
        db_query = db_query.filter(models.Answers.name == name)
    if mobile:
        db_query = db_query.filter(models.Answers.mobile == mobile)
    if theme:
        db_query = db_query.filter(models.Answers.theme == theme)
    return db_query.count(), db_query.order_by(models.Answers.createat.desc()).offset(limit * (skip - 1)).limit(
        limit).all()


def create(db: Session, answers: answers_schema.AnswersCreate):
    """新增"""
    db_answers = models.Answers(name=answers.name, mobile=answers.mobile, gender=answers.gender,
                                theme=answers.theme, level=answers.level, createat=int(round(time.time() * 1000)))
    db.add(db_answers)
    db.commit()
    db.refresh(db_answers)
    return db_answers


def get_by_id(db: Session, pk: str):
    """通过编号获取数据"""
    return db.query(models.Answers).filter(models.Answers.id == pk).first()


def userlist(db: Session, name: str, mobile: str, skip: int = 1, limit: int = 10):
    """查询用户"""
    db_query = db.query(models.Answers.name,
                        models.Answers.mobile, models.Answers.gender)
    if name:
        db_query = db_query.filter(models.Answers.name == name)
    if mobile:
        db_query = db_query.filter(models.Answers.mobile == mobile)
    db_query = db_query.distinct(
        models.Answers.name, models.Answers.mobile, models.Answers.gender)
    return db_query.count(), db_query.offset(limit * (skip - 1)).limit(limit).all()


def get_by_name_and_mobile(db: Session, name: str, mobile: str) -> models.Answers:
    """通过姓名和电话获取数据"""
    return db.query(models.Answers).from_statement(text("""SELECT b.* FROM (SELECT MAX( id ) AS id FROM answers GROUP BY name,mobile,theme) AS a INNER JOIN answers AS b ON a.id = b.id WHERE b.name=:name and b.mobile=:mobile""")).params(name=name, mobile=mobile).all()
