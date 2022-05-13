#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : minidata.
# @File         : x
# @Time         : 2022/4/11 下午6:21
# @Author       : yuanjie
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  :


from meutils.pipe import *

get_resolve_path = lambda path, file=__file__: (Path(os.path.dirname(file)) / Path(path)).resolve()


print(get_resolve_path('../../nesc', __file__))
print(get_module_path('../../nesc', __file__))
