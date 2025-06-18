from typing import Callable, Dict, List


class EventEmitter[T]:
    def __init__(self):
        self._listeners: Dict[str, List[Callable]] = {}

    def on(self, event_name: T, handler: Callable):
        if event_name not in self._listeners:
            self._listeners[event_name] = []
        self._listeners[event_name].append(handler)

    def off(self, event_name: T, handler: Callable):
        if event_name not in self._listeners:
            return
        try:
            self._listeners[event_name].remove(handler)
            if not self._listeners[event_name]:
                del self._listeners[event_name]
        except ValueError:
            pass 

    def emit(self, event_name: T, *args, **kwargs):
        if event_name not in self._listeners:
            return
        for handler in self._listeners[event_name]:
            handler(*args, **kwargs)