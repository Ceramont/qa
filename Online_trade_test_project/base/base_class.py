import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver


    """Method Get Current URL"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current url {get_url}")

    """Method word Assert"""
    def assert_word(self, value, expected):
        value_word = value.text
        assert value_word == expected
        print("Value succeed")

    """Method Screenshot"""
    def screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = f'screenshot_{now_date}.png'
        self.driver.save_screenshot(
            '..\\screenshots\\' + name_screenshot)

    """Method assert URL"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        print("asd:" + get_url)
        assert get_url == result
        print("Good value URL")
