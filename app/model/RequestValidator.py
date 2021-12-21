class RequestValidator:

    def __init__(self, redisConection):
        self.redisConection = redisConection

    def increment(self, request, configuration):
        pathCount = int(self.redisConection.incrby(request.path()))
        ipCount = int(self.redisConection.incrby(request.ip()))
        ipPathCount = int(self.redisConection.incrby(request.ip() + request.path()))

        if pathCount > configuration.max_path():
            return self.fail_increment(request, "se excedio el limite de llamadas a {}".format(request.path()))

        if ipCount > configuration.max_ip():
            return self.fail_increment(request, "se excedio el limite de llamadas a {}".format(request.ip()))

        if ipPathCount > configuration.max_ip_path():
            return self.fail_increment(request, "se excedio el limite de llamadas a {} con la ip {}".format(request.path(), request.ip()))

    def fail_increment(self, request, log):
        request.set_log(log)
        request.set_status(-1)

