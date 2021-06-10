from page_objects.login_page import LoginPage, RegistrationPage
import globals
import config


class TestSignUpIn:
    """ Class with test methods for checking user SignUp and SignIn"""
    def test_sign_up(self, driver, generate_login):
        """
        Test method for user signing up
        :param driver: driver instance
        :param generate_login: (str) generated user email
        """
        sign_up = RegistrationPage(driver)
        sign_up.check_registration_form()
        sign_up.register_user(email=generate_login, password=config.PASSWORD, first_mame=globals.FIRST_NAME,
                              second_name=globals.SECOND_NAME)
        sign_up.check_and_compare_email_address(email=generate_login)
        sign_up.confirm_email(email=config.MAIL, password=config.PASSWORD, support_mail=config.SUPPORT_MAIL)
        sign_up.check_user_logged_in()

    def test_sign_in(self, driver, generate_login):
        """
        Test method for user signing in
        :param driver: driver instance
        :param generate_login: (str) generated user email
        """
        sign_up = LoginPage(driver=driver)
        sign_up.check_login_form()
        sign_up.login_user(email=generate_login, password=config.PASSWORD)
        sign_up = RegistrationPage(driver=driver)
        sign_up.check_user_logged_in()
