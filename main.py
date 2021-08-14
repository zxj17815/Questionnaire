#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2021/08/13 13:54:22
@Author  :   JayZhang 
@Version :   1.0
@Contact :   597952291@qq.com
@License :   (C)Copyright 2021, iceiceice
@Desc    :   None
'''

# here put the import lib

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from controllers.answers import router as answers_router
# here put the main code


app = FastAPI(title="Questionnaire",version="1.0.0")


# 跨资源共享
origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(answers_router)

