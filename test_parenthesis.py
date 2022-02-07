import unittest
import parenthesis as ps



class TestStringMethods(unittest.TestCase):
    def test_success(self):
        success = """()
        (())
        (())()
        ((()))((()))"""

        for ln in success.split('\n'):
            arr = [s for s in ln.strip()]
            # It's a well formed situation, so outcome should be True
            self.assertTrue(ps.balanced(arr))
        
    def test_mismatched_parenthesis(self):
        success = """(()}
        {)"""

        for ln in success.split('\n'):
            arr = [s for s in ln.strip()]
            # The inner function should throw the expected exception.
            with self.assertRaises(ps.ParenthesisError) as context:
                ps.parse(arr)
            self.assertTrue("Mismatched closing" in context.exception.args[0])
            # ... and if we call the wrapper, the outcome should be False
            self.assertFalse(ps.balanced(arr))

    def test_imbalanced_parenthesis(self):
        
        failure = """(
        )()(
        ((()()()()
        ((())))((((()"""
        for ln in failure.split('\n'):
            arr = [s for s in ln.strip()]
            # The inner function should throw the expected exception.
            with self.assertRaises(ps.ParenthesisError) as context:
                ps.parse(arr)
            self.assertTrue("Imbalanced" in context.exception.args[0])
            # It's a badly formed situation, so outcome should be False
            self.assertFalse(ps.balanced(arr))
