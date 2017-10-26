class ClockGenerator:
    def __init__(self, clock_config):
        self.events = []
        for event_name in clock_config['events']:
            self.events.append(Event(event_name))

    def get_event(self, name):
        for event in self.events:
            if event.name == name:
                return event

    def subscribe(self, event_name, listener):
        event = self.get_event(event_name)
        event.add_subscriber(listener)

    def run(self):
        while True:
            for event in self.events:
                event.fire()


class Event:
    def __init__(self, name):
        self.name = name
        self.subscribers = []

    def __repr__(self):
        return self.name

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def fire(self):
        for subscriber in self.subscribers:
            subscriber.clock_event(self.name)


class ClockListener:
    def clock_event(self, event_name):
        raise NotImplementedError
