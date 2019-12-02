import unittest
from app.models import Users
class UserModelTest(unittest.TestCase):
    ''''
    Test case to see if users and their passwords are being saved
    '''
    
    def setUp(self):
        self.new_user = User(password='mypass')
        
    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_word is not None)
        
    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password
            
    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('mypass'))