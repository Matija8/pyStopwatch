import sys
from src.timer_subject import TimerSubject
from src.timer_gui import TimerGui
from src.timer_gui_observable_adapter import TimerGuiObserverAdapter
from src.cli_observer import CliTimerObserver


def _gui_main():
    timer, gui = TimerSubject(), TimerGui()
    gui.set_toggle_btn_command(timer.toggle_timer)
    gui.set_reset_btn_command(timer.reset_timer)
    observer = TimerGuiObserverAdapter(gui)
    observer.sub(timer)
    timer.set_time_update()
    gui.start_gui()
    timer.clear_time_update()


def _cli_main():
    timer = TimerSubject()
    try:
        cli = CliTimerObserver()
        print(
            'Commands:\n Press enter to toggle timer on/off.\n Press Ctrl+c to exit.'
        )
        timer.set_time_update()
        input()
        cli.sub(timer)
        while True:
            timer.toggle_timer()
            if timer.running:
                print('Stopwatch started')
            else:
                print('Stopwatch stopped')
            input()
    except KeyboardInterrupt:
        print('\n')
        timer.clear_time_update()
        print('Bye!')


if __name__ == '__main__':
    use_cli = '-c' in sys.argv[1:]
    if use_cli:
        _cli_main()
    else:
        _gui_main()
