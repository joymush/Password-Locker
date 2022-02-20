import unittest
from password_locker import generate_password
import pyperclip
from user_credentials import User, Credential

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: helps in creating test cases
    '''
    def setUp(self):
        '''
        Function to create a user account before each test
        '''
        self.new_user = User('Joy','Chemutai','Joy1424,')

    def test_init_(self):
        '''
        Test to if check the initialization/creation of user instances is properly done
        '''
        self.assertEqual(self.new_user.first_name,'Joy')
        self.assertEqual(self.new_user.last_name,'Chemutai')
        self.assertEqual(self.new_user.password,'Joy1424,')

    def test_save_user(self):
        '''
        Test to check if the new users info is saves into the users list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.

    Aargs:
         unittest.TestCase: helps in creating test cases
    '''
    def test_check_user(self):
            '''
            Function to test whether the login in function check_user works as expected
            '''
            self.new_user = User('Joy','Chemutai','Joy1424,')
            self.new_user.save_user()
            user2 = User('Derrick','Bett','Joy1424,')
            user2.save_user()

            for user in User.users_list:
                    if user.first_name == user2.first_name and user.password == user2.password:
                        current_user = user.first_name
            return current_user

            self.assertEqual(current_user,Credential.check_user(user2.password,user2.first_name))

    def setUp(self):
        '''
        Function to create an account's credentials before each test
        '''
        self.new_credential = Credential('Joy','Facebook','Joytashy','Joy1424')

    def test_init_(self):
         '''
         Test to if check the initialization/creation of credential instances is properly done
         '''
         self.assertEqual(self.new_credential.user_name,'Joy')
         self.assertEqual(self.new_credential.site_name,'Facebook')
         self.assertEqual(self.new_credential.account_name,'Joytashy')
         self.assertEqual(self.new_credential.password,'Joy1424,')

    def test_save_credentials(self):
         '''
         Test to check if the new credential info is saved into the credentials list
         '''
         self.new_credential.save_credentials()
         twitter = Credential('Foster','Twitter','mushfoster','Joy1424,')
         twitter.save_credentials()
         self.assertEqual(len(Credential.credentials_list),2)

    #def test_generate_password(self):
         '''
         Test to check if the generate password generates 8 character long alphanumeric numbers
         '''
         self.twitter = Credential('Twitter', 'mushfoster','')
         self.twitter.password = generate_password()
         self.assertEqual()

    def tearDown(self):
         '''
         Function to clear the credentials list after every test
         '''
         Credential.credentials_list = []
         User.users_list = []

    def test_display_credentials(self):
        '''
        Test to check if the display_credentials method, displays the correct credentials.
        '''
        self.new_credential.save_credentials()
        twitter = Credential('foster','Twitter','mushfoster','Joy1424,')
        twitter.save_credentials()
        gmail = Credential('foster','Gmail','mushfoster','Joy1424,')
        gmail.save_credentials()
        self.assertEqual(len(credits.find_by_site_name('Twitter')),2)

    def test_find_by_site_name(self):
        '''
        Test to check if the find_by_site_name method returns the correct credential
        '''
        self.new_credential.save_credentials()
        twitter = Credential('foster','Twitter','mushfoster','Joy1424,')
        twitter.save_credentials()
        credential_exists = Credential.find_by_site_name('Twitter')
        self.assertEqual(credential_exists,twitter)

    def test_copy_credential(self):
        '''
        Test to check if the copy a credential method copies the correct credential
        '''
        self.new_credential.save_credentials()
        twitter = Credential('foster','Twitter','mushfoster','Joy1424,')
        twitter.save_credentials()
        find_credential = None
        for credential in Credential.user_credentials_list:
                         find_credential =Credential.find_by_site_name(credential.site_name)
                         return pyperclip.copy(find_credential.password)
        Credential.copy_credential(self.new_credential.site_name)
        self.assertEqual('Joy1424,',pyperclip.paste())
        print(pyperclip.paste())

if __name__ == '_main_':
     unittest.main(verbosity=2)

