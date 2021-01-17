import tkinter as tk
from typing import Callable
from .time_format import TimeFormatter as tf


class TimerGui:

    TimeLabelFont = ('Verdana', 20)
    ToggleBtnFont = ('Verdana', 10)

    def __init__(self):
        self._root = TimerGui._make_root()
        self._toggleBtn = TimerGui._make_toggle_btn(self._root)
        self._resetBtn = TimerGui._make_reset_btn(self._root)
        self._timeLabel = TimerGui._make_time_label(self._root)

    def set_time(self, time_in_seconds: float) -> None:
        self._timeLabel['text'] = TimerGui._format_time(time_in_seconds)

    def set_toggle_btn_command(self, callback: Callable[[], None]) -> None:
        self._toggleBtn.configure(command=callback)

    def set_reset_btn_command(self, callback: Callable[[], None]) -> None:
        self._resetBtn.configure(command=callback)

    def start_gui(self):
        self._root.mainloop()

    def set_on_destroy_hook(self, callback: Callable[[], None]):
        def on_destroy():
            callback()
            self._root.destroy()

        self._root.protocol('WM_DELETE_WINDOW', on_destroy)

    @staticmethod
    def _make_root() -> tk.Tk:
        root = tk.Tk()
        root.title('Stopwatch')
        width, height = 400, 300
        root.geometry(f'{width}x{height}')
        root.minsize(width, height)
        return root

    @staticmethod
    def _make_toggle_btn(root: tk.Tk) -> tk.Button:
        btn = tk.Button(
            root,
            text='Toggle on/off',
            font=TimerGui.ToggleBtnFont,
            command=lambda: print('No command set!')
        )
        btn.pack(pady=30, side=tk.TOP)
        return btn

    @staticmethod
    def _make_reset_btn(root: tk.Tk) -> tk.Button:
        btn = tk.Button(
            root,
            text='Reset',
            font=TimerGui.ToggleBtnFont,
            command=lambda: print('No command set!')
        )
        btn.pack(pady=20, side=tk.TOP)
        return btn

    @staticmethod
    def _make_time_label(root: tk.Tk) -> tk.Label:
        time_label = tk.Label(
            root, text='', bg='black', fg='white', font=TimerGui.TimeLabelFont
        )
        time_label.pack(pady=5)
        time_label['text'] = TimerGui._format_time(0)
        return time_label

    @staticmethod
    def _format_time(time_in_seconds: float) -> str:
        return tf.format_time_with_ms(time_in_seconds)
