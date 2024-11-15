class Data:
    def __init__(self, data: str, ip: int) -> None:
        self.data = data
        self.ip = ip


class Server:
    server_count = 0

    def __new__(cls, *args, **kwargs):
        cls.server_count += 1
        return super().__new__(cls)

    def __init__(self):
        self.ip = self.server_count
        self.buffer: list[Data] = []

    def send_data(self, data: Data) -> None:
        self.router.buffer.append(data)

    def get_data(self) -> list:
        res = self.buffer.copy()
        self.buffer.clear()
        return res

    def get_ip(self) -> int:
        return self.ip


class Router:
    __instance = False

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.buffer: list[Data] = []
        self.servers: list[Server] = []

    def link(self, server: Server) -> None:
        if server not in self.servers:
            self.servers.append(server)
            server.router = self

    def unlink(self, server: Server) -> None:
        if server in self.servers:
            self.servers.remove(server)
            del server.__dict__["router"]

    def send_data(self) -> None:
        for data in self.buffer:
            for server in self.servers:
                if data.ip == server.ip:
                    server.buffer.append(data)
        self.buffer.clear()
