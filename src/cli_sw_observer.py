from .observer import Observer
from .time_format import TimeFormatter as tf


class CliSwObserver(Observer):
    def update(self, time_value: float) -> None:
        print(f'\r{CliSwObserver.format(time_value)}', end='')

    @staticmethod
    def format(time_in_seconds: float) -> str:
        return tf.format_time_with_ms(time_in_seconds)
