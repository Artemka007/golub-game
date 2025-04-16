from typing import Any, Callable


class Observable[TValue]:
    def __init__(self):
        self._subscribers = set[Callable[[TValue], Any]]()

    def subscribe(self, callback: Callable[[TValue], Any]):
        self._subscribers.add(callback)

    def unsubscribe(self, callback: Callable[[TValue], Any]):
        self._subscribers.discard(callback)