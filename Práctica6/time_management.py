
class Time:
    def __init__(self, hora=12, minuto=0, segundo=0):
        self._hora = hora
        self._minuto = minuto
        self._segundo = segundo
    
    def __str__(self):
        periodo = "AM" if self._hora < 12 else "PM"
        hora_12 = self._hora if self._hora <= 12 else self._hora - 12
        if hora_12 == 0:
            hora_12 = 12
        return f"{hora_12:02d}:{self._minuto:02d}:{self._segundo:02d} {periodo}"
    
    def set_time(self, hora, minuto, segundo, formato="24 HOURS"):
        if 0 <= hora <= 23 and 0 <= minuto <= 59 and 0 <= segundo <= 59:
            self._hora = hora
            self._minuto = minuto
            self._segundo = segundo
            return True
        return False
    
    def get_time(self):
        periodo = "AM" if self._hora < 12 else "PM"
        hora_12 = self._hora if self._hora <= 12 else self._hora - 12
        if hora_12 == 0:
            hora_12 = 12
        
        return {
            'hours': self._hora,
            'minutes': self._minuto,
            'seconds': self._segundo,
            'format': f"{periodo}"
        }
    
    @property
    def hora(self):
        return self._hora
    
    @property
    def minuto(self):
        return self._minuto
    
    @property
    def segundo(self):
        return self._segundo
    
    @hora.setter
    def hora(self, valor):
        if 0 <= valor <= 23:
            self._hora = valor
    
    @minuto.setter
    def minuto(self, valor):
        if 0 <= valor <= 59:
            self._minuto = valor
    
    @segundo.setter
    def segundo(self, valor):
        if 0 <= valor <= 59:
            self._segundo = valor