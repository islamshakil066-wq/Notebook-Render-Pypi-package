class InvalidURLException(Exception):
    def __init__(self, message=" URL is not valid."):
        self.message = message
        super().__init__(self.message)