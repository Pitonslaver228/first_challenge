class Server:
    server_count = 0

    def __new__(cls, *args, **kwargs):
        cls.server_count += 1
        return super().__new__(cls)


class Router:
    pass


class Data:
    def __init__(self, data: str, ip: int) -> None:
        self.data = data
        self.ip = ip
