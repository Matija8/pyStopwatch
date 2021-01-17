from .observer import Observer


class CliTimerObserver(Observer):
    def update(self, time_value: float) -> None:
        print(f'\r{time_value:.4}', end='')
