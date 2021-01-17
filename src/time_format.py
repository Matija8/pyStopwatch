import unittest


class TimeFormatter():
    @staticmethod
    def format_time_with_ms(time_in_seconds: float) -> str:
        regular_time = TimeFormatter.format_time(time_in_seconds)
        ms_time = TimeFormatter._format_miliseconds(time_in_seconds)
        return f'{regular_time}:{ms_time}'

    @staticmethod
    def format_time(time_in_seconds: float) -> str:
        time_in_seconds_floor = int(time_in_seconds)
        seconds = time_in_seconds_floor % 60
        minutes = time_in_seconds_floor // 60 % 60
        hours = time_in_seconds_floor // (60 * 60) % 24
        assert seconds < 60 and minutes < 60 and hours < 24
        seconds_str = TimeFormatter._add_leading_zero_if_needed(str(seconds))
        minutes_str = TimeFormatter._add_leading_zero_if_needed(str(minutes))
        hours_str = TimeFormatter._add_leading_zero_if_needed(str(hours))
        return f'{hours_str}:{minutes_str}:{seconds_str}'

    @staticmethod
    def _add_leading_zero_if_needed(val: str) -> str:
        assert len(val) in [1, 2]
        if len(val) == 1:
            return '0' + val
        return val

    @staticmethod
    def _format_miliseconds(time_in_seconds: float) -> str:
        ms_str = str(float(time_in_seconds) % 1)[2:6]
        assert len(ms_str) <= 4
        ms_str = ms_str + '0' * (4 - len(ms_str))
        return ms_str


class TestFormatTimeCase(unittest.TestCase):
    def test_simple_times(self):
        self.assertEqual(TimeFormatter.format_time(120), '00:02:00')

    def test_whole_times_vs_datetime_timedelta(self):
        from datetime import timedelta
        seconds_in_day = 86400
        for time_in_seconds in range(0, seconds_in_day, 54):
            timedelta_time = str(timedelta(seconds=time_in_seconds))
            if len(timedelta_time) < 8:
                timedelta_time = '0' + timedelta_time
            self.assertEqual(
                TimeFormatter.format_time(time_in_seconds), timedelta_time
            )

    def test_simple_times_with_ms(self):
        self.assertEqual(
            TimeFormatter.format_time_with_ms(120), '00:02:00:0000'
        )


if __name__ == '__main__':
    unittest.main()
