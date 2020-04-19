import unittest
from core import utils
import logging as lg

logger = lg.getLogger(__name__)


class MyTestCase(unittest.TestCase):
    def test_log_level(self):
        logger_before = logger
        utils.set_logger()
        logger_after = logger
        self.assertEqual(logger_before, logger_after)

        lg.info('Test log info')
        lg.debug('Test log debug')
        lg.warning('Test log warning')
        lg.critical('Test log Critical')


if __name__ == '__main__':
    unittest.main()
