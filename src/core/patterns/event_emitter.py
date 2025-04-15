from typing import Callable


class EventEmitter[T]:
    def __init__(self):
        self._listeners = {}

    def on(self, event_name: T, handler: Callable):
        if event_name not in self._listeners:
            self._listeners[event_name] = []
        self._listeners[event_name].append(handler)

    def emit(self, event_name: T, *args, **kwargs):
        if event_name not in self._listeners:
            return
        for handler in self._listeners[event_name]:
            handler(*args, **kwargs)