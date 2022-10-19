class Break:
    def __init__(self, start, end, duration):
        self.start = start
        self.end = end
        self.duration = duration
    def __str__(self):
        return str(self.start) + ", " + str (self.end) +", "+ str(self.duration)

