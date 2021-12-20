class ProxyRequest:

    def __init__(self, request):
        self.request = request
        self.status = 1
        self.startTime = ''
        self.endTime = ''
        self.log = ''

    def ip(self):
        ip = self.request.remote_addr
        return ip

    def path(self):
        return self.request.path

    def set_log(self, aStringLog):
        self.log = aStringLog

    def set_status(self, numeric_value):
        self.status = numeric_value

    def get_log(self):
        return self.log

    # Persistencia en MongoDb
    def store(self):
        return self

    def is_valid(self):
        return self.status != -1