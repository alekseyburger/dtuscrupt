# GNU GENERAL PUBLIC LICENSE
# Autor: Aleksey Burger

class ExceptionDevice(Exception):
    def __init__(self, message, snap):
        self.message = message
        self.snap = snap
    def __str__(self):
        return f"{self.message}\n{self.snap}"