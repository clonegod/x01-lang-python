#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging.config

import yaml

def setup_logging(
    default_path='logging.yaml',
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """Setup logging configuration

    """
    path = default_path
    # 从环境变量中读取日志配置文件
    value = os.getenv(env_key, None)
    if value:
        path = value
    print '............log file path:%s' % path
    # 如果指定的日志配置文件存在，则使用该文件来配置logger
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    # 否则，使用默认配置
    else:
        logging.basicConfig(level=default_level)