import tkinter as tk
from datetime import timedelta
from typing import Callable
import time
import threading


class TimerGui:

    TimeLabelFont = ('Verdana', 20)
    ToggleBtnFont = ('Verdana', 10)

    def __init__(self):
        self._root = TimerGui._make_root()
        self._set_close_hook()
        self._toggleBtn = TimerGui._make_toggle_btn(self._root)
        self._timeLabel = TimerGui._make_time_label(self._root)
        self._time_update_thread = None
        self._should_join_signal = False

    def set_time(self, time_in_seconds: float) -> None:
        self._timeLabel['text'] = str(timedelta(seconds=int(time_in_seconds)))

    def set_toggle_btn_command(self, callback: Callable[[], None]) -> None:
        self._toggleBtn.configure(command=callback)

    def start_gui(self):
        self._root.mainloop()

    def set_time_update(self, time_getter: Callable[[], float]) -> None:
        self.clear_time_update()

        def time_update():
            while True:
                if self._should_join_signal:
                    break
                self.set_time(time_getter())
                WAIT_SECONDS = 0.1
                time.sleep(WAIT_SECONDS)

        self._time_update_thread = threading.Thread(target=time_update)
        self._time_update_thread.start()
        print('Interval update thread started!')

    def clear_time_update(self) -> None:
        if self._time_update_thread:
            _debug_threads()
            self._should_join_signal = True
            self._time_update_thread.join()
            self._time_update_thread = None
            print('Join success!')
            self._should_join_signal = False
            _debug_threads()

    def _set_close_hook(self):
        def on_destroy():
            self.clear_time_update()
            self._root.destroy()

        self._root.protocol('WM_DELETE_WINDOW', on_destroy)

    @staticmethod
    def _make_root() -> tk.Tk:
        root = tk.Tk()
        root.title('Timer')
        root.geometry('300x200')
        root.minsize(300, 200)
        return root

    @staticmethod
    def _make_toggle_btn(root: tk.Tk) -> tk.Button:
        btn = tk.Button(
            root,
            text='Toggle timer',
            font=TimerGui.ToggleBtnFont,
            command=lambda: print('No command set!')
        )
        btn.pack(pady=30, side=tk.TOP)
        return btn

    @staticmethod
    def _make_time_label(root: tk.Tk) -> tk.Label:
        time_label = tk.Label(
            root, text='', bg='black', fg='white', font=TimerGui.TimeLabelFont
        )
        time_label.pack(pady=5)
        time_label['text'] = str(timedelta(seconds=0))
        return time_label


def _debug_threads():
    print('Active threads:')
    for thread in threading.enumerate():
        print('\t' + thread.name)
