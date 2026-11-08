import re

class Time:

    TIME_FORMATS = ("AM", "PM", "24 HOURS")
    time_count = 0 

    def __init__(self, hours: int = 12, minutes: int = 0, seconds: int = 0, time_format: str = "AM"):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
        self._time_format = time_format.upper()
        Time.time_count += 1

    @property
    def hours(self) -> int:
        return self._hours

    @hours.setter
    def hours(self, hours: int):
        self._hours = hours

    @property
    def minutes(self) -> int:
        return self._minutes

    @minutes.setter
    def minutes(self, minutes: int):
        self._minutes = minutes

    @property
    def seconds(self) -> int:
        return self._seconds

    @seconds.setter
    def seconds(self, seconds: int):
        self._seconds = seconds

    @property
    def time_format(self) -> str:
        return self._time_format

    @time_format.setter
    def time_format(self, time_format: str):
        self._time_format = time_format.upper()

    @classmethod
    def is_valid_format(cls, time_format: str):
        return time_format.upper() in cls.TIME_FORMATS

    def _assign_format(self, time_format: str):
        if self.is_valid_format(time_format):
            self._time_format = time_format.upper()
            return True
        return False

    def is_valid_time(self) -> bool:
        if self._time_format in ("AM", "PM"):
            if not (1 <= self._hours <= 12):
                return False
        elif self._time_format == "24 HOURS":
            if not (0 <= self._hours <= 23):
                return False
        else:
            return False
            
        if not (0 <= self._minutes <= 59):
            return False
        if not (0 <= self._seconds <= 59):
            return False
        return True

    @classmethod
    def from_string(cls, time_string: str):
        time_string = time_string.strip()
        patron = r"^(\d{1,2}):(\d{2}):(\d{2})(?:\s+(.*))?$"
        match = re.match(patron, time_string)
        
        if match:
            hours = int(match.group(1))
            minutes = int(match.group(2))
            seconds = int(match.group(3))
            if not match.group(4):
                return None
            time_format = match.group(4)
            
            if cls.is_valid_format(time_format):
                instancia = cls(hours, minutes, seconds, time_format)
                if instancia.is_valid_time():
                    return instancia
                    
        return None