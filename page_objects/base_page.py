from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EXPLICITLY_WAIT_TIMEOUT = 10


class BasePage:
    """
    Class with Base methods
    """

    def __init__(self, driver, timeout=EXPLICITLY_WAIT_TIMEOUT):
        """
        BasePage constructor
        :param driver: driver instance
        :param timeout: an argument that indicates how long to wait
        """
        self.driver = driver
        self.driver.implicitly_wait(timeout)

    def is_element_present(self, how, what, timeout=EXPLICITLY_WAIT_TIMEOUT):
        """
        Basic method of checking that an element isn't present
        :param how: an argument that indicates how to search (css, id, xpath и i.e.)
        :param what: an argument that indicates what to search for (selector string)
        :param timeout: an argument that indicates how long to wait
        :return:  bool. return True if the element is present else it will return False
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def wait_and_click(self, how, what, timeout=EXPLICITLY_WAIT_TIMEOUT):
        """
        Basic method to wait until button be clickable and click it
        :param how: an argument that indicates how to search (css, id, xpath и i.e.)
        :param what: an argument that indicates what to search for (selector string)
        :param timeout: an argument that indicates how long to wait
        """
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((how, what)))
        element.click()

    def get_element_text(self, how, what, timeout=EXPLICITLY_WAIT_TIMEOUT):
        """
        Basic method to get text of the element
        :param how: an argument that indicates how to search (css, id, xpath и i.e.)
        :param what: an argument that indicates what to search for (selector string)
        :param timeout: an argument that indicates how long to wait
        """
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((how, what)))
        element_text = self.driver.find_element(how, what).text
        return element_text

    def send_text_to_element(self, how, what, text, timeout=EXPLICITLY_WAIT_TIMEOUT):
        """
        Basic method to send text to elements
        :param how: an argument that indicates how to search (css, id, xpath и i.e.)
        :param what: an argument that indicates what to search for (selector string)
        :param text: an argument that indicates by what text search element (string)
        :param timeout: an argument that indicates how long to wait
        """
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((how, what)))
        element.send_keys(text)
