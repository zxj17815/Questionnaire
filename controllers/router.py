#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   router.py
@Time    :   2021/08/13 14:21:34
@Author  :   JayZhang 
@Version :   1.0
@Contact :   597952291@qq.com
@License :   (C)Copyright 2021, iceiceice
@Desc    :   None
'''

# here put the import lib
from fastapi import APIRouter
from . import answers
# here put the main code


router = APIRouter(
    prefix="/answers",
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

router.include_router(answers.router)  # 回答
