import time

import pytest

from Pages.l_page import LaunchPage


@pytest.mark.usefixtures("setup")
class TestSkypeLogin:
    def test_successful_login(self):
        lp = LaunchPage(self.driver)
        lp.sign_button()
        lp.email_enter("dev1.intellify@gmail.com")
        lp.code_email()
        lp.Otp()
        time.sleep(5)
        lp.FCE()
