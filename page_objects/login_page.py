from page_objects.base_page import BasePage
from locators.login_locators import SignUpLocators, SignInLocators
import time
import pytest
from imbox import Imbox
import re


def get_confirm_code(email, password, support_mail):
    """
    Function responsible for getting account confirmation code and confirm letter deletion
    :param password: (str) account password
    :param email: (str) account initial email
    :param support_mail: (str) eos support mail
    :return: confirmation code for account registration
    """
    confirm_code = None
    for _ in range(10):
        time.sleep(3)
        with Imbox('imap.gmail.com',
                   username=email,
                   password=password,
                   ssl=True,
                   ssl_context=None,
                   starttls=False) as imbox:
            all_inbox_messages = imbox.messages(sent_from=support_mail)
            for uid, message in all_inbox_messages:
                confirm_code = re.search(r'\d{2}-\d{2}', str(message.body)).group(0).replace("-", "")
                print(confirm_code)
                imbox.delete(uid)
        if confirm_code is not None:
            break
    if confirm_code is None:
        pytest.fail("Confirmation mail is not received")
    return confirm_code


class RegistrationPage(BasePage):
    def check_registration_form(self):
        """
        Method for sign in form checking
        """
        assert self.is_element_present(*SignUpLocators.SIGN_UP_FORM_ACTIVE), "Sign Up form should be selected by " \
                                                                             "default"
        assert self.is_element_present(*SignUpLocators.FIRST_NAME_FORM), "The 'First Name' field is not present"
        assert self.is_element_present(*SignUpLocators.SECOND_NAME_FORM), "The 'Second Name' field is not present"
        assert self.is_element_present(*SignUpLocators.EMAIL_FORM), "The 'Email' field is not present"
        assert self.is_element_present(*SignUpLocators.PASSWORD_FORM), "The 'Password' field is not present"
        assert self.is_element_present(*SignUpLocators.TERMS_OF_USE), "The 'Term of use' checkbox is not present"
        assert self.is_element_present(*SignUpLocators.SIGN_UP_BTN), "The 'SignUp' button is not present"

    def register_user(self, email, password, first_mame, second_name):
        """
        Method for account registration
        :param email: (str) generated email
        :param password: (str) account password
        :param first_mame: (str) account first name
        :param second_name: (str) account second name
        :return:
        """
        self.send_text_to_element(*SignUpLocators.FIRST_NAME_FORM, text=first_mame)
        self.send_text_to_element(*SignUpLocators.SECOND_NAME_FORM, text=second_name)
        self.send_text_to_element(*SignUpLocators.EMAIL_FORM, text=email)
        self.send_text_to_element(*SignUpLocators.PASSWORD_FORM, text=password)
        self.wait_and_click(*SignUpLocators.TERMS_OF_USE)
        time.sleep(2)
        self.wait_and_click(*SignUpLocators.SIGN_UP_BTN)

    def check_and_compare_email_address(self, email):
        """
        Method for checking generated email
        :param email: (str) generated email
        """
        login = self.get_element_text(*SignUpLocators.VERIFY_EMAIL)
        assert email == login, f'email {login} is shown instead {email}'

    def confirm_email(self, email, password, support_mail):
        """
        Method for email confirmation
        :param password: (str) account password
        :param email: (str) account initial email
        :param support_mail: (str) eos support mail
        """
        confirm_code = get_confirm_code(email, password, support_mail)
        self.send_text_to_element(*SignUpLocators.CONFIRMATION_CODE, text=confirm_code)
        assert self.is_element_present(*SignUpLocators.CONFIRM_MAIL_BTN)

    def check_user_logged_in(self):
        """
        Method for checking that user is logged in
        """
        assert self.is_element_present(*SignUpLocators.MY_ACCOUNT)


class LoginPage(BasePage):
    def check_login_form(self):
        """
        Method for checking log in form
        """
        self.wait_and_click(*SignInLocators.SIGN_IN_FORM)
        assert self.is_element_present(*SignInLocators.SIGN_IN_FORM_ACTIVE), "Sign In form should be selected by "
        assert self.is_element_present(*SignUpLocators.EMAIL_FORM), "The 'Email' field is not present"
        assert self.is_element_present(*SignUpLocators.PASSWORD_FORM), "The 'Password' field is not present"
        time.sleep(2)
        assert self.is_element_present(*SignInLocators.SIGN_IN_BTN), "The 'SignUp' button is not present"

    def login_user(self, email, password):
        """
        Method for user logging in
        :param password: (str) account password
        :param email: (str) account initial email
        """
        self.send_text_to_element(*SignUpLocators.EMAIL_FORM, text=email)
        self.send_text_to_element(*SignUpLocators.PASSWORD_FORM, text=password)
        time.sleep(2)
        self.wait_and_click(*SignInLocators.SIGN_IN_BTN)
