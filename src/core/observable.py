class Subject:
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def notify_observers(self, *args, **kwargs):
        for observer in self._observers:
            observer.update(*args, **kwargs)

class Observer:
    def update(self, *args, **kwargs):
        pass