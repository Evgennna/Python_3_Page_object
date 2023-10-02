import time

import pytest
from testpage import OperationHelper
username = "29103740"
password = "39d8bf048b"

def test_step_1(browser):
    test_page1 = OperationHelper(browser)
    test_page1.go_to_site()
    test_page1.enter_login("29103740")
    test_page1.enter_pswd("39d8bf048b")
    test_page1.click_button()
    time.sleep(3)
  
    test_page1.click_contact()
    time.sleep(3)
    
    test_page1.enter_cont_name("29103740")
    test_page1.enter_cont_email("mail@mail.ru")
    test_page1.enter_cont_text("Hi, how are you?")
    time.sleep(1)
    
    test_page1.click_button()
    time.sleep(1)

    assert test_page1.get_alert_text() == "Form successfully submitted"
