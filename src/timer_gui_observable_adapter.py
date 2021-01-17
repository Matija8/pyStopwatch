from .timer_gui import TimerGui
from .observer import Observer


class TimerGuiObserverAdapter(Observer):
    def __init__(self, timer_gui: TimerGui) -> None:
        super().__init__()
        self.timer_gui = timer_gui
        self.timer_gui.set_on_destroy_hook(self.unsub)

    def update(self, new_time) -> None:
        self.timer_gui.set_time(new_time)
