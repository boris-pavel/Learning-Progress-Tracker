import unittest
import task


class TestTask(unittest.TestCase):

    def test_check_email(self):
        # tests for the check_email() function
        self.assertTrue(task.check_email("abcd@gmail.com"))
        self.assertFalse(task.check_email("abcd"))

    def test_check_doubles(self):
        # tests for the check_doubles() function
        self.assertTrue(task.check_doubles("''"))
        self.assertTrue(task.check_doubles("-'"))
        self.assertTrue(task.check_doubles("Blabla--"))

        self.assertFalse(task.check_doubles("BlaBla"))

    def test_check_name(self):
        # test for the check_name() function
        self.assertTrue(task.check_name("Boris"))
        self.assertTrue(task.check_name("O'Neil"))
        self.assertTrue(task.check_name("Jean-Claude"))
        self.assertTrue(task.check_name("Robert Jemison Van de Graaff"))

        self.assertFalse(task.check_name("O'Neil'"))
        self.assertFalse(task.check_name("Jean--Claude"))
        self.assertFalse(task.check_name("~D0MInAt0R~"))
        self.assertFalse(task.check_name("~D0MInAt0R~ Boss"))
        self.assertFalse(task.check_name("-Boris-"))
        self.assertFalse(task.check_name("D."))


