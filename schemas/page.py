#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   page.py
@Time    :   2021/08/13 15:20:55
@Author  :   JayZhang 
@Version :   1.0
@Contact :   597952291@qq.com
@License :   (C)Copyright 2021, iceiceice
@Desc    :   None
'''

# here put the import lib

from typing import Any, List

from pydantic import BaseModel

# here put the main code

class PageBase(BaseModel):
    """列表数据基本序列"""
    page: int
    page_size: int
    count: int
    data: List[Any]