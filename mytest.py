import unittest
from myfunction import my_perm

class MyTest(unittest.TestCase):
    def test(self):
        # enter the word
        functionlist = my_perm('aaba')
        # enter the correct list of anagrams
        mylist = ['aba','baa','aab']
        self.assertEqual(sorted(functionlist), sorted(mylist))


if __name__ == '__main__':
    unittest.main(exit=False)