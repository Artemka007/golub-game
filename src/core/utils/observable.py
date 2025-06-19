from typing import Any, Callable, TypeVar


T = TypeVar('T')


class Observable[T]:
    def __init__(self):
        self._subscribers = set[Callable[[T], Any]]()

    def subscribe(self, callback: Callable[[T], Any]):
        self._subscribers.add(callback)

    def unsubscribe(self, callback: Callable[[T], Any]):
        self._subscribers.discard(callback)