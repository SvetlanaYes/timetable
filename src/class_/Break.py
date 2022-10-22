class Break:
    def __init__(self, start, end, duration):
        self.start = start
        self.end = end
        self.duration = duration

    def __str__(self):
        return str(self.start) + ", " + str(self.end) + ", " + str(self.duration)

    def __eq__(self, other):
        if self.start == other.start and self.end == other.end and self.duration == other.duration:
            return True
        else:
            return False