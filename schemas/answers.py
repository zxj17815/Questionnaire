#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   answers.py
@Time    :   2021/08/13 14:41:37
@Author  :   JayZhang 
@Version :   1.0
@Contact :   597952291@qq.com
@License :   (C)Copyright 2021, iceiceice
@Desc    :   回答序列化
'''

# here put the import lib

from pydantic import BaseModel, Field

# here put the main code


class AnswersBase(BaseModel):
    """问卷数据基本序列"""
    name: str = Field(...,title="姓名", max_length=4)
    mobile: str = Field(...,title="电话", max_length=13)
    gender: int = Field(...,title="性别",gt=0,le=1)
    theme: int = Field(...,title="问卷主题",gt=1,le=7)
    level: int = Field(...,title="评级",gt=1,le=5)
    score: int = Field(...,title="分数",gt=0,le=100)

    class Config:
        orm_mode = True


class AnswersCreate(AnswersBase):
    """新增序列"""

    class Config:
        orm_mode = True


class AnswersView(AnswersBase):
    """查看"""
    id: int = Field(...)
    createat: int=Field(None,title="时间戳",)

    class Config:
        orm_mode = True
