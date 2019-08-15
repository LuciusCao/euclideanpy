class BaseElement(object):
    def __init__(self, symbol, explicit=True, alias=None, hook=None):
        if not isinstance(symbol, str):
            raise Exception("symbol of element must be string")
        elif not symbol.isalpha():
            raise Exception("symbol must be represented as a letter")

        if (not alias is None) and (not isinstance(alias, str)):
            raise Exception("alias must be string")

        self.name = symbol
        self.explicit = explicit
        self.alias = alias
        self.hook = hook

    def __repr__(self):
        return self.__class__.__name__ + ': ' + self.name

    def _hook_graph(self, graph):
        g_name = graph.name
        if g_name != self.hook:
            self.hook = graph
        else:
            raise Exception('{}: hook already existed'.format(self.name))
