import unittest
import json
from .. import app
from ..utils import fibonacci


class BenchTestCase(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()
        self.logger = app.app.logger

    def tearDown(self):
        pass

    def test_fib(self):
        self.logger.info("Testing  Fibonacci numbers")
        fib_numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i, fib_number in enumerate(fib_numbers):
            self.assertEqual(fibonacci.fibonacci(i), fib_number, msg="fib({}) = {}?".format(i, fib_number))
        print("Can get fib(30)?")
        fibonacci.fibonacci(30)
        print("Yes")

    def test_hello_world(self):
        self.logger.info("Testing Hello world")
        hello_world_response = self.app.get('/hello_world')
        self.assertEqual(hello_world_response._status_code, 200)
        self.assertEqual({"hello": "World"}, json.loads(hello_world_response.data.decode()))

    def test_hello_user(self):
        self.logger.info("Testing Hello user")
        hello_user_response = self.app.get('/hello/user')
        self.assertEqual(hello_user_response._status_code, 200)
        self.assertEqual({"hello": "user"}, json.loads(hello_user_response.data.decode()))

    def test_fib30(self):
        self.logger.info("Testing fibonacci 30")
        fib30_response = self.app.get('/fib30')
        self.assertEqual(fib30_response._status_code, 200)
        self.assertEqual({"fibonacci30": 1346269}, json.loads(fib30_response.data.decode()))


if __name__ == '__main__':
    unittest.main()
