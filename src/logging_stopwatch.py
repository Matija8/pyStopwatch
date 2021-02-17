from datetime import datetime
from os import mkdir

from .simple_stopwatch import Stopwatch
from pathlib import Path


class LoggingSW(Stopwatch):
    def __init__(self):
        super().__init__()
        self._should_log = True
        self.logfile_name = 'sw-log'
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
        seconds = Stopwatch.seconds_since_epoch()
        formated_time = LoggingSW.format_seconds(seconds)
        date = LoggingSW.seconds_to_date(seconds)
        self._log(f'{text}\t{formated_time}', date)

    def _log(self, text: str, date: str) -> None:
        if not self._should_log:
            return
        # print(text)
        if self.logfile_name:
            log_dir = './logs'
            Path(log_dir).mkdir(parents=True, exist_ok=True)
            logfile_name = f'{log_dir}/{self.logfile_name} {date}.txt'
            with open(logfile_name, 'a') as f:
                f.write(text + '\n')

    @staticmethod
    def format_seconds(seconds_since_epoch: float) -> str:
        time = datetime.fromtimestamp(seconds_since_epoch)
        # format_string = '%H:%M:%S on date: %Y.%m.%d'
        format_string = '%H:%M on date %Y.%m.%d'
        return time.strftime(format_string)

    @staticmethod
    def seconds_to_date(seconds_since_epoch: float) -> str:
        time = datetime.fromtimestamp(seconds_since_epoch)
        format_string = '%Y-%m-%d'
        return time.strftime(format_string)
