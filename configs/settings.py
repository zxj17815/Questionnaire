#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   settings.py
@Time    :   2021/08/13 14:27:00
@Author  :   JayZhang 
@Version :   1.0
@Contact :   597952291@qq.com
@License :   (C)Copyright 2021, iceiceice
@Desc    :   None
'''

# here put the import lib

import os

# here put the main code


# 获取环境变量
env = os.getenv("ENV", "")
if env:
    # 如果有虚拟环境 则是且为POR 并存在生产配置对应文件-> 生产环境
    if env == 'POR' and os.path.exists('settings/settings_por.py'):
        print("----------生产环境启动------------")
        from configs.por import settings
    else:
        # 不为POR则-> 开发环境
        print("----------开发环境启动------------")
        from configs.dev import settings
else:
    # 没有则-> 开发环境
    print("----------开发环境启动------------")
    from configs.dev import settings
