import threading
import time
from typing import List, Union

from .observer import Observer
from .simple_stopwatch import Stopwatch


class StopwatchSubject():

    WAIT_SECONDS = 0.1  # type: float

    def __init__(self, sw: Stopwatch):
        self.sw = sw
        self._observers = []  # type: List[Observer]
        self._time_update_thread = None  # type: Union[threading.Thread, None]
        self._should_join_signal = False

    def sub(self, observer):
        # print('Sub added to TimerSubject')
        self._observers.append(observer)
        return self

    def unsub(self, observer_to_unsub):
        self._observers.remove(observer_to_unsub)

    def notify_observers(self):
        elapsed_time = self.sw.get_elapsed_time()
        for observer in self._observers:
            observer.update(elapsed_time)

    def set_time_update(self) -> None:
        self.clear_time_update()

        def time_update():
            while True:
                if self._should_join_signal:
                    break
                self.notify_observers()
                time.sleep(StopwatchSubject.WAIT_SECONDS)

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


def _debug_threads():
    print('Active threads:')
    for i, thread in enumerate(threading.enumerate()):
        print(f'   {i}) {thread.name}')
