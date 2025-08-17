class Register:
    @property
    def value(self) -> int:
        raise NotImplementedError

    @value.setter
    def value(self, value) -> None:
        raise NotImplementedError
