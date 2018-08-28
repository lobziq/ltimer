from datetime import datetime, timedelta


class Timer:
    def __init__(self, **kwargs):
        self.start_time = datetime.utcnow()
        self.finish_time = self.start_time + timedelta(**kwargs)

    def is_finished(self):
        return not self.is_alive()

    def is_alive(self):
        return True if self.finish_time > datetime.utcnow() else False