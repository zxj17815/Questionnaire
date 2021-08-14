#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   answers.py
@Time    :   2021/08/13 14:18:22
@Author  :   JayZhang 
@Version :   1.0
@Contact :   597952291@qq.com
@License :   (C)Copyright 2021, iceiceice
@Desc    :   None
'''

# here put the import lib

from sqlalchemy.sql.expression import null
from schemas.page import PageBase
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from database import get_db_dep
from dao import answers as answers_dao
from schemas import answers as answers_schema

# here put the main code


router = APIRouter(
    prefix="",
    tags=["orm product"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=PageBase, name='获取列表')
def read(page: int = 1, page_size: int = 10, name: str = None, mobile: str = None, db: Session = Depends(get_db_dep)):
    """
    获取结果列表  \n
    - **page**: 当前页数 默认为1
    - **page_size**: 每页数量 默认10
    - **name**: 姓名
    - **mobile**: 电话
    \f
    :param page:
    :param page_size:
    :param name:
    :param mobile:
    :param db:
    :return:
    """
    count, answers = answers_dao.list(
        db, skip=page, limit=page_size, name=name, mobile=mobile,)
    data = PageBase(page=page, page_size=page_size, count=count,
                    data=[answers_schema.AnswersView.from_orm(answer) for answer in answers])
    return data


@router.post("/", response_model=answers_schema.AnswersCreate, name='新增')
def create(answer: answers_schema.AnswersCreate, db: Session = Depends(get_db_dep)):
    """
    新增 \n
    \f
    """
    return answers_dao.create(db, answers=answer)
