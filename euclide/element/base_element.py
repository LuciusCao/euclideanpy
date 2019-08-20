from ..validations import symbol_validation


class BaseElement(object):
    def __init__(self, symbol, explicit=True, alias=None, hook=None):
        _ = symbol_validation(symbol)

        self.symbol = symbol
        self.name = symbol
        self.explicit = explicit
        self.alias = alias
        self.hook = hook

    def __repr__(self):
        return self.__class__.__name__ + ': ' + self.name

    def hook_graph(self, graph):
        g_name = graph.name
        if g_name != self.hook:
            self.hook = graph
        else:
            raise Exception('{}: hook already existed'.format(self.name))
