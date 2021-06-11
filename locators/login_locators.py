from selenium.webdriver.common.by import By


class SignUpLocators:
    SIGN_UP_FORM = (By.XPATH, "//button[contains(@data-id, 'go-signup-btn')]")
    SIGN_UP_FORM_ACTIVE = (By.XPATH, "//button[contains(@data-id, 'go-signup-btn') and contains(@class, 'checked')]")
    FIRST_NAME_FORM = (By.XPATH, "//*[contains(@data-id, 'first_name')]")
    SECOND_NAME_FORM = (By.XPATH, "//*[contains(@data-id, 'last_name')]")
    EMAIL_FORM = (By.XPATH, "//input[contains(@data-id, 'email')]")
    PASSWORD_FORM = (By.XPATH, "//*[contains(@data-id, 'password') and contains(@class, 'password-input')]")
    TERMS_OF_USE = (By.XPATH, "//*[contains(@data-id, 'policy_confirm')]//input[contains(@type, 'checkbox')]/..")
    SIGN_UP_BTN = (By.XPATH, "//button[contains(@data-id, 'sign-up-btn')]")
    VERIFY_EMAIL = (By.XPATH, "//ui-confirm-email//*[contains(@class, 'email')]")
    CONFIRMATION_CODE = (By.XPATH, "//*[contains(@data-id, 'confirm-code-input')]")
    RESEND_MAIL_BTN = (By.XPATH, "//button[contains(@data-id, 'resend-code-btn')]")
    CONFIRM_MAIL_BTN = (By.XPATH, "//button[contains(@data-id, 'submit-code-btn')]")
    MY_ACCOUNT = (By.XPATH, "//button[contains(@data-id, 'sidebar-user-menu')]")


class SignInLocators:
    SIGN_IN_FORM = (By.XPATH, "//button[contains(@data-id, 'sign-in-button')]")
    SIGN_IN_FORM_ACTIVE = (By.XPATH, "//button[contains(@data-id, 'sign-in-button') and contains(@class, 'checked')]")
    SIGN_IN_BTN = (By.XPATH, "//button[contains(@data-id, 'sign-in-btn')]")
