from unittest import TestCase

from hamcrest import assert_that, equal_to
from project_code.hello import Hello


class TestHello(TestCase):
    def test_world_returns_hello_followed_by_passed_in_person(self):
        hello = Hello()
        assert_that(hello.world("name"), equal_to("hello name"))
