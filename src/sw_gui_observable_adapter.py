from .observer import Observer
from .sw_gui import StopwatchGui


class SwGuiToObserverAdapter(Observer):
    def __init__(self, timer_gui: StopwatchGui) -> None:
        super().__init__()
        self.timer_gui = timer_gui
        self.timer_gui.set_on_destroy_hook(self.unsub)

    def update(self, new_time) -> None:
        self.timer_gui.set_time(new_time)
