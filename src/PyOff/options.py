from abc import ABC, abstractmethod


class AbsOption(ABC):
    @abstractmethod
    def __init__(self, kind, strike, maturity):
        self.kind = kind
        self.strike = strike
        self.maturity = maturity

    @abstractmethod
    def payoff(self, spot):
        pass


class Call(AbsOption):
    def __init__(self, strike, maturity):
        super().__init__("call", strike, maturity)

    def payoff(self, spot):
        return max(spot - self.strike, 0)


class Put(AbsOption):
    def __init__(self, strike, maturity):
        super().__init__("put", strike, maturity)

    def payoff(self, spot):
        return max(self.strike - spot, 0)


if __name__ == "__main__":
    my_call = Call(100, 1)
    my_put = Put(100, 1)
    print(my_call.payoff(110))
    print(my_put.payoff(90))
