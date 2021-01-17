import sys

from src.cli_sw_observer import CliSwObserver
from src.logging_stopwatch import LoggingSW
from src.sw_gui import StopwatchGui
from src.sw_gui_observable_adapter import SwGuiToObserverAdapter
from src.sw_subject import StopwatchSubject


def _gui_main():
    sw_subject, gui = StopwatchSubject(LoggingSW()), StopwatchGui()
    gui.set_toggle_btn_command(sw_subject.sw.toggle_timer)
    gui.set_reset_btn_command(sw_subject.sw.reset_timer)
    observer = SwGuiToObserverAdapter(gui)
    observer.sub(sw_subject)
    sw_subject.set_time_update()
    gui.start_gui()
    sw_subject.clear_time_update()


def _cli_main():
    sw_subject = StopwatchSubject(LoggingSW())
    try:
        cli = CliSwObserver()
        print(
            'Commands:\n Press enter to toggle timer on/off.\n Press Ctrl+c to exit.'
        )
        sw_subject.set_time_update()
        input()
        cli.sub(sw_subject)
        while True:
            sw_subject.sw.toggle_timer()
            if sw_subject.sw.running:
                print('Stopwatch started')
            else:
                print('Stopwatch stopped')
            input()
    except KeyboardInterrupt:
        print('\n')
        sw_subject.clear_time_update()
        print('Bye!')


if __name__ == '__main__':
    use_cli = '-c' in sys.argv[1:]
    if use_cli:
        _cli_main()
    else:
        _gui_main()
