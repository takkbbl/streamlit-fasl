class Authentication:
    def __init__(self):
        self.authenticated = False

    # TODO: Validate subscription key
    def is_valid_subscription_key(self, api_key: str) -> bool:
        if api_key != "123":
            self.authenticated = False
            return False
        self.authenticated = True
        return True
