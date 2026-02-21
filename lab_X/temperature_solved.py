class Temperature:

    CONVERTERS = {
        "KK": lambda t: t,
        "KC": lambda t: t - 273.15,
        "KF": lambda t: t * 9 / 5 - 459.67,
        "CK": lambda t: t + 273.15,
        "CC": lambda t: t,
        "CF": lambda t: t * 9 / 5 + 32,
        "FK": lambda t: (t + 459.67) * 5 / 9,
        "FC": lambda t: (t - 32) * 5 / 9,
        "FF": lambda t: t,
    }

    def __init__(self, value=0, unit="K"):
        self.value = value
        self.unit = unit

    def __repr__(self):
        return f"Temperature({self.value}, '{self.unit}')"

    def __str__(self):
        if self.unit == "K":
            return f"{self.value} K"
        else:
            return f"{self.value}\u00B0{self.unit}"

    def convert(self, unit):
        key = self.unit + unit
        self.value = self.CONVERTERS[key](self.value)
        self.unit = unit
