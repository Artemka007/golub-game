from src.core.patterns.observable import Observable


class Subject[TValue](Observable[TValue]):
    _value: TValue

    def subscribe(self, callback):
        super().subscribe(callback)
        callback(self._value)

    def next(self, value: TValue):
        self._value = value
        for callback in self._subscribers:
            callback(value)
    
    def get_value(self):
        return self._value
    
    def as_observable(self):
        class ObservableView(Observable[TValue]):
            def __init__(self, subject: Subject[TValue]):
                super().__init__()
                self._subscribers = subject._subscribers

        return ObservableView(self)
