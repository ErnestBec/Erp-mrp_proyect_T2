class NotFoundException(Exception):
    def __init__(self, item):
        super().__init__(*args)
