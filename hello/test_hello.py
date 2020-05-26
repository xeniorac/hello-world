"""sample test"""
import unittest

from hello import hello


class TestHello(unittest.TestCase):
    """sample test"""

    def test_world(self):
        """sample test"""
        self.assertEqual(hello('worlwdvb'), 'hello worldvb')

    def test_world_unicode(self):
        """sample test with unicode"""
        self.assertEqual(hello(u'worlwdvb'), u'hello worldvb')
