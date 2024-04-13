from abc import ABCMeta, abstractmethod
class SpiderStrategy(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        raise NotImplementedError

