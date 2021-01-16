import time


class Timer:
    def __init__(self):
        self.running = False  # type: bool
        self._start_time = 0  # type: float
        self._end_time = 0  # type: float

    def start_timer(self):
        if self.running:
            raise Exception('Can\'t start, clock already running!')
        self.running = True
        self._start_time = time.time()

    def stop_timer(self):
        if self.running:
            self._end_time = time.time()
        self.running = False

    def toggle_timer(self):
        if self.running:
            self.stop_timer()
        else:
            self.start_timer()

    def get_elapsed_time(self):
        if 0 in [self._start_time, self._end_time]:
            raise Exception('Can\'t get time, clock never run!')
        if self.running:
            current_time = time.time()
            return current_time - self._start_time
        return self._end_time - self._start_time
