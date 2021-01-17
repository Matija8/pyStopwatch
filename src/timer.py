import time


class Timer:
    def __init__(self):
        self.running = False  # type: bool
        self._last_start_time = 0  # type: float
        self._elapsed_time = 0  # type: float

    def start_timer(self):
        if not self.running:
            self._last_start_time = Timer.seconds_since_epoch()
            self.running = True

    def stop_timer(self):
        if self.running:
            end_time = Timer.seconds_since_epoch()
            self._elapsed_time += end_time - self._last_start_time
            self.running = False

    def reset_timer(self):
        self.running = False
        self._last_start_time = 0
        self._elapsed_time = 0  # type: float

    def toggle_timer(self):
        print('Toggle')
        if self.running:
            self.stop_timer()
        else:
            self.start_timer()

    def get_elapsed_time(self):
        if self.running:
            current_time = Timer.seconds_since_epoch()
            passing_time = current_time - self._last_start_time
            return passing_time + self._elapsed_time
        return self._elapsed_time

    @staticmethod
    def seconds_since_epoch():
        return time.time()
