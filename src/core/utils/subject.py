from typing import TypeVar
from src.core.utils.observable import Observable


T = TypeVar('T')


class Subject[T](Observable[T]):
    _value: T

    def subscribe(self, callback):
        super().subscribe(callback)
        callback(self._value)

    def next(self, value: T):
        self._value = value
        for callback in self._subscribers:
            callback(value)
    
    def get_value(self):
        return self._value
    
    def as_observable(self):
        class ObservableView(Observable[T]):
            def __init__(self, subject: Subject[T]):
                super().__init__()
                self._subscribers = subject._subscribers

        return ObservableView(self)
