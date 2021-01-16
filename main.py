from src.timer import Timer
from src.timer_gui import TimerGui


def _gui_main():
    timer, timer_gui = Timer(), TimerGui()
    timer_gui.set_toggle_btn_command(_make_toggle_callback(timer, timer_gui))
    timer_gui.set_time_update(lambda: timer.get_elapsed_time())
    timer_gui.start_gui()


def _make_toggle_callback(timer: Timer, timer_gui: TimerGui):
    def callback():
        timer.toggle_timer()
        timer_gui.set_time(timer.get_elapsed_time())
        print(f'Timer is running: {timer.running}')

    return callback


def _cli_main():
    t = Timer()
    try:
        print(
            'Commands:\n Press enter to toggle timer on/off.\n Press Ctrl+c to exit.'
        )
        input()
        while True:
            t.toggle_timer()
            if t.running:
                print('Timer started')
            else:
                print('Timer stopped')
                print(f'{t.get_elapsed_time():.2f} seconds have passed.')
            input()
    except KeyboardInterrupt:
        print('Bye!')


if __name__ == '__main__':
    use_cli = False
    if use_cli:
        _cli_main()
    else:
        _gui_main()
