class Observer():
    def __init__(self) -> None:
        self.subscription = None

    def sub(self, subject) -> None:
        self.subscription = subject.sub(self)

    def unsub(self) -> None:
        if self.subscription:
            self.subscription.unsub(self)
            self.subscription = None

    def update(self, value) -> None:
        raise NotImplementedError()
