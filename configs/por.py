#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   por.py
@Time    :   2021/08/13 14:28:20
@Author  :   JayZhang 
@Version :   1.0
@Contact :   597952291@qq.com
@License :   (C)Copyright 2021, iceiceice
@Desc    :   None
'''

# here put the import lib
from pydantic import BaseSettings


# here put the main code


class Settings(BaseSettings):
    DATABASE = {
        'questionnaire': 'mysql://root@127.0.0.1/questionnaire?charset=utf8',
    }


# 实例化配置对象
settings = Settings()
