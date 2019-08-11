class BaseElement:
    def __init__(self, symbol, explicit=True, alias=None, hooks=set()):
        if not isinstance(symbol, str):
            raise Exception("symbol of element must be string")
        elif not symbol.isalpha():
            raise Exception("symbol must be represented as a letter")

        if (not alias is None) and (not isinstance(alias, str)):
            raise Exception("alias must be string")

        self.name = symbol
        self.explicit = explicit
        self.alias = alias
        self.hooks = hooks

    def __repr__(self):
        return self.__class__.__name__ + ': ' + self.name

    def hook_graph(self, graph):
        self.hooks.add(graph)
