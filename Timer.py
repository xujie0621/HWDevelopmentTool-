import datetime
class time:

    def compareTime(self, start, end, log):
        start_t = datetime.datetime.strptime(start, '%m-%d %H:%M:%S.%f')
        end_t = datetime.datetime.strptime(end, '%m-%d %H:%M:%S.%f')
        log_t = datetime.datetime.strptime(log, '%m-%d %H:%M:%S.%f')

        if (log_t >= start_t and log_t <= end_t):
            return True

    def subTime(self, start, log):
        start_t = datetime.datetime.strptime(start, '%m-%d %H:%M:%S.%f')
        log_t = datetime.datetime.strptime(log, '%m-%d %H:%M:%S.%f')
        dif_t = (log_t - start_t)
        return dif_t.microseconds / 1000000 + dif_t.seconds
