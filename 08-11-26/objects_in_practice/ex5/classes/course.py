class Course:
    def __init__(self, code, name, capacity):
        self.code = code
        self.name = name
        self.capacity = capacity
        self.registered = []
        self.waiting = []

    def enroll(self, name):
        if name in self.registered or name in self.waiting:
            raise ValueError(f"{name} is already registered")
        if len(self.registered) < self.capacity:
            self.registered.append(name)
            return f"enrolled"
        else:
            self.waiting.append(name)
            return f"waitlisted"

    def __str__(self):
        return f"{self.code} {self.name} | {len(self.registered)}/{self.capacity} enrolled | waitlist: {len(self.waiting)}"



