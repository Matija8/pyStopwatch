from src.timer import Timer


def _main():
    t = Timer()
    while True:
        input('Press enter to start timer.')
        t.start_timer()
        input('Press enter to stop timer.')
        t.stop_timer()
        print(f'Passed: {t.get_elapsed_time():.2f} seconds')


if __name__ == '__main__':
    _main()
