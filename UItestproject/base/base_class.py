

class Base():

    def __init__(self, driver):
        self.driver = driver


    """Method Get Current URL"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current url {get_url}")

    """Method Assert"""
    def assert_word(self, value, expected):
        value_word = value.text
        assert value_word == expected
        print("Value succeed")
