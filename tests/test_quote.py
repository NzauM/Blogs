import unittest
from app.models import Quote

Quote = quote.Quote

class QuoteTest(unittest.TestCase):
    '''
    This test class tests the behavior of the quote clas
    '''

    def setUp(self):
        '''
        The setup method will run befor every test
        '''
        self.new_quote = Quotes(12, 'Every day the sun rises' ,'Mercy Nzau')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quote))

if __name__ == '__main__':
    unittest.main()