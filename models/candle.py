from __future__ import annotations

from . import _base


class Candle(_base.Model):
    swagger_types: dict[str, str] = {
        'figi': 'str',
        'interval': 'CandleResolution',
        'o': 'float',
        'c': 'float',
        'h': 'float',
        'l': 'float',
        'v': 'int',
        'time': 'datetime',
    }

    attribute_map: dict[str, str] = {
        'figi': 'figi',
        'interval': 'interval',
        'o': 'o',
        'c': 'c',
        'h': 'h',
        'l': 'l',
        'v': 'v',
        'time': 'time',
    }

    def __init__(
        self,
        figi=None,
        interval=None,
        o=None,
        c=None,
        h=None,
        l=None,
        v=None,
        time=None,
    ):
        self._figi = None
        self._interval = None
        self._o = None
        self._c = None
        self._h = None
        self._l = None
        self._v = None
        self._time = None
        self.discriminator = None
        self.figi = figi
        self.interval = interval
        self.o = o
        self.c = c
        self.h = h
        self.l = l
        self.v = v
        self.time = time

    @property
    def figi(self):
        """
        :rtype: str
        """
        return self._figi

    @figi.setter
    def figi(self, figi):
        """
        :param str figi:
        """
        if figi is None:
            raise ValueError('Invalid value for `figi`, must not be `None`')

        self._figi = figi

    @property
    def interval(self):
        """
        :rtype: clients.tinkoff.models.CandleResolution
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """
        :param clients.tinkoff.models.CandleResolution interval:

        """
        if interval is None:
            raise ValueError(
                'Invalid value for `interval`, must not be `None`'
            )

        self._interval = interval

    @property
    def o(self):
        """
        :rtype: float
        """
        return self._o

    @o.setter
    def o(self, o):
        """
        :param float o:
        """
        if o is None:
            raise ValueError('Invalid value for `o`, must not be `None`')

        self._o = o

    @property
    def c(self):
        """
        :rtype: float
        """
        return self._c

    @c.setter
    def c(self, c):
        """
        :param float c:
        """
        if c is None:
            raise ValueError('Invalid value for `c`, must not be `None`')

        self._c = c

    @property
    def h(self):
        """
        :rtype: float
        """
        return self._h

    @h.setter
    def h(self, h):
        """
        :param float h:
        """
        if h is None:
            raise ValueError('Invalid value for `h`, must not be `None`')

        self._h = h

    @property
    def l(self):
        """
        :rtype: float
        """
        return self._l

    @l.setter
    def l(self, l):
        """
        :param float l:
        """
        if l is None:
            raise ValueError('Invalid value for `l`, must not be `None`')

        self._l = l

    @property
    def v(self):
        """
        :rtype: int
        """
        return self._v

    @v.setter
    def v(self, v):
        """
        :param int v:
        """
        if v is None:
            raise ValueError('Invalid value for `v`, must not be `None`')

        self._v = v

    @property
    def time(self):
        """
        ISO8601
        :rtype: datetime.datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        ISO8601
        :param datetime.datetime time:
        """
        if time is None:
            raise ValueError('Invalid value for `time`, must not be `None`')

        self._time = time
