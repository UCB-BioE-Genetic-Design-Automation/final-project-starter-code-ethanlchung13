class Sample:

    def __init__(self, construct: str, concentration: str, culture: str):
        self.construct = construct
        self.concentration = concentration
        self.label = construct + " " + concentration
        self.side_label = construct
        self.culture = culture
        self.location = None

    def get_construct(self):
        return self.construct

    def get_concentration(self):
        return self.concentration

    def get_label(self):
        return self.label

    def get_side_label(self):
        return self.side_label

    def get_culture(self):
        return self.culture

    def get_location(self):
        return self.location
