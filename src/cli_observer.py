from .observer import Observer
from .time_format import TimeFormatter as tf


class CliTimerObserver(Observer):
    def update(self, time_value: float) -> None:
        print(f'\r{CliTimerObserver.format(time_value)}', end='')

    @staticmethod
    def format(time_in_seconds: float) -> str:
        return tf.format_time_with_ms(time_in_seconds)
