class Server:
    server_count = 0

    def __new__(cls, *args, **kwargs):
        cls.server_count += 1
        return super().__new__(cls)

    def __init__(self):
        self.ip = self.server_count


class Router:
    __instance = False

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.buffer: list[Data] = []
        self.servers: list[Server] = []


class Data:
    def __init__(self, data: str, ip: int) -> None:
        self.data = data
        self.ip = ip
