#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)

class Person():
    def __init__(self, name, age, country=u'中国'):
        self.name = name
        self.age = age
        self.country = country
    
    def getInfo(self):
        logger.info('name=%s,age=%d,country=%s' % (self.name, self.age, self.country))
    
    def tryError(self):
        try:
            open('/path/to/does/not/exist', 'rb')
        except (SystemExit, KeyboardInterrupt):
            raise
        except Exception, e:
            logger.error('Failed to open file', exc_info=True)

if __name__ == '__main__':
    print 'Run test...'
    alice = Person('alice', 20)
    alice.getInfo()
