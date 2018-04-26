#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
#import loggingCfgJson
import loggingCfgYAML
import clonegod.person as person

#loggingCfgJson.setup_logging()
loggingCfgYAML.setup_logging()
logger = logging.getLogger(__name__)


logger.info('app start run')
alice = person.Person('alice', 20)
alice.getInfo()
alice.tryError()
logger.info('app execute over')