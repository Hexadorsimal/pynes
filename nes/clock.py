class ClockGenerator:
    def __init__(self, clock_config):
        self.listeners = []
        self.events = []
        for event_name in clock_config['events']:
            self.events.append(Event(event_name))

    def add_listener(self, listener):
        self.listeners.append(listener)

    def run(self):
        while True:
            for event in self.events:
                for listener in self.listeners:
                    listener.clock_tick(event.name)


class Event:
    def __init__(self, name):
        self.name = name


class ClockListener:
    def clock_tick(self, event_name):
        raise NotImplementedError
