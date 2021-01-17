import time


class Stopwatch:
    def __init__(self):
        self.running = False  # type: bool
        self._last_start_time = 0  # type: float
        self._elapsed_time = 0  # type: float

    def toggle_timer(self):
        if self.running:
            self._stop_timer()
        else:
            self._start_timer()

    def reset_timer(self):
        self.running = False
        self._last_start_time = 0
        self._elapsed_time = 0  # type: float

    def get_elapsed_time(self):
        if self.running:
            current_time = Stopwatch.seconds_since_epoch()
            passing_time = current_time - self._last_start_time
            return passing_time + self._elapsed_time
        return self._elapsed_time

    def _start_timer(self):
        assert not self.running
        start_time = Stopwatch.seconds_since_epoch()
        self._last_start_time = start_time
        self.running = True

    def _stop_timer(self):
        assert self.running
        end_time = Stopwatch.seconds_since_epoch()
        self._elapsed_time += end_time - self._last_start_time
        self.running = False

    @staticmethod
    def seconds_since_epoch():
        return time.time()
