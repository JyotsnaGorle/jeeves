import abc

class BaseStrategy:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def describe(self):
        """The derived strategy class should implement this to display the description"""

    @abc.abstractmethod
    def perform(self):
        """The derived strategy class should implement this carry out the strategy"""

    @abc.abstractmethod
    def react(self):
        """The derived strategy class should implement this to react accordingly"""
