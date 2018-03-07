from time import clock

UNITS = {'s': 1, 'ms': 1000, 'm': 1/60, 'h': 1/3600}


class Timer:
    """
    # code-timer
        A class to measure time elapsed and count number of passes through code segments
        using time.clock()
        Useful for benchmarking and code improvement.

        >>> t = Timer()  # starts the timer object
        ...
        >>> t.stop()  # stops the timer object
        >>> t.total  # then contains total time between creation and stop() in seconds.
        >>> repr(t)  # returns time with units as string, so print(t) can be used.

        >>> t = Timer(wait=True)  # creates timer but doesn't start measuring. t can be passed to functions to measure time
        Wait is False by default. See previous case.

        >>> t.start()  # begins measuring.
        ...
        >>> t.stop()  # stops measuring.
        ...
        >>> t.start() # starts measuring again
        ...
        >>> t.stop()  # stops measuring
        >>> t.total  # now has total time recorded between starts and stops in seconds
        >>> t.count  # contains number of times the timer was triggered

        This can be used in a loop to measure time per loop or count number of times a function was called.

        >>> t = Timer(unit='s')  # to define what units to print the time in.

        Options are 's' (second), 'ms' (millisecond), 'm' (minute) and 'h' (hour).

        By default the unit is 'ms' but in a project the default units can be set before all usages by

        >>> Timer.default_unit = 's'  # or any unit
    """
    default_unit = 'ms'

    def __init__(self, **kwargs):
        try:
            self.unit = kwargs['unit']
        except KeyError:
            self.unit = self.default_unit
        self.count = 0
        self.total = 0
        self._start = 0
        self.is_running = False
        try:
            if not kwargs['wait']:
                self.start()
        except KeyError:
            self.start()

    def start(self):
        if not self.is_running:
            self.count += 1
            self.is_running = True
            self._start = clock()

    def stop(self):
        if self.is_running:
            self.total += clock() - self._start
            self.is_running = False

    def reset(self):
        self.is_running = False
        self.count = 0
        self.total = 0
        self._start = 0

    def __repr__(self):
        return str(round(self.total*UNITS[self.unit], 4)) + ' ' + self.unit
