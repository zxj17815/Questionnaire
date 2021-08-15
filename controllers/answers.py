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

from typing import List
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
    tags=["Answers"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=PageBase, name='获取列表')
def read(page: int = 1, page_size: int = 10, name: str = None, mobile: str = None, theme: str = None, db: Session = Depends(get_db_dep)):
    """
    获取结果列表  \n
    - **page**: 当前页数 默认为1
    - **page_size**: 每页数量 默认10
    - **name**: 姓名
    - **mobile**: 电话
    - **theme**: 问卷主题
    \f
    :param page:
    :param page_size:
    :param name:
    :param mobile:
    :param theme:
    :param db:
    :return:
    """
    count, answers = answers_dao.list(
        db, skip=page, limit=page_size, name=name, mobile=mobile, theme=theme)
    data = PageBase(page=page, page_size=page_size, count=count,
                    data=[answers_schema.AnswersView.from_orm(answer) for answer in answers])
    return data


@router.get("/alltheme", response_model=PageBase, name='获取问卷主题合并列表')
def alltheme(page: int = 1, page_size: int = 10, name: str = None, mobile: str = None, db: Session = Depends(get_db_dep)):
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
    count, answers = answers_dao.userlist(
        db, skip=page, limit=page_size, name=name, mobile=mobile)
    commbo = []
    for item in answers:
        one_data = answers_dao.get_by_name_and_mobile(
            db, name=item.name, mobile=item.mobile)
        if one_data:
            commbo.append(answers_schema.AnswersOneData(
                name=item.name, mobile=item.mobile, theme_list=one_data))
    data = PageBase(page=page, page_size=page_size, count=count,
                    data=commbo)
    return data


@router.get("/one", response_model=answers_schema.AnswersOneData, name='获取一个人所有最新的各个主题问卷数据')
def readone(name: str, mobile: str, db: Session = Depends(get_db_dep)):
    """
    获取结果列表  \n
    - **name**: 姓名
    - **mobile**: 电话
    \f
    :param name:
    :param mobile:
    :param db:
    :return:
    """
    data = answers_dao.get_by_name_and_mobile(db, name=name, mobile=mobile)
    if data:
        res = answers_schema.AnswersOneData(
            name=name, mobile=mobile, theme_list=data)
        return res
    else:
        raise HTTPException(status_code=400, detail={"msg": "data not found"})


@router.post("/", status_code=201, response_model=answers_schema.AnswersCreate, name='新增')
def create(answer: answers_schema.AnswersCreate, db: Session = Depends(get_db_dep)):
    """
    新增 \n
    \f
    """
    try:
        return answers_dao.create(db, answers=answer)
    except Exception as e:
        raise HTTPException(status_code=400, detail={"msg": str(e)})
