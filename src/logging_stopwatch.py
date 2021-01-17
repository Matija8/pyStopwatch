from datetime import datetime

from .simple_stopwatch import Stopwatch


class LoggingSW(Stopwatch):
    def __init__(self):
        super().__init__()
        self._should_log = True
        self.logfile_name = 'sw-log.txt'
        self._log_with_current_time('Open')

    def reset_timer(self):
        super().reset_timer()
        self._log_with_current_time('Reset')

    def _start_timer(self):
        super()._start_timer()
        self._log_with_current_time('Start')

    def _stop_timer(self):
        super()._stop_timer()
        self._log_with_current_time('Stop')

    def _log_with_current_time(self, text: str) -> None:
        self._log(
            f'{text}\t{LoggingSW.format_seconds(Stopwatch.seconds_since_epoch())}'
        )

    def _log(self, text: str) -> None:
        if not self._should_log:
            return
        # print(text)
        if self.logfile_name:
            with open(self.logfile_name, 'a') as f:
                f.write(text + '\n')

    @staticmethod
    def format_seconds(seconds_since_epoch: float) -> str:
        time = datetime.fromtimestamp(seconds_since_epoch)
        # format_string = '%H:%M:%S on date: %Y.%m.%d'
        format_string = '%H:%M on date %Y.%m.%d'
        return time.strftime(format_string)
