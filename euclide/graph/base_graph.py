from ..element.point import Point
from ..element.segment import Segment


class BaseGraph(object):
    def __init__(self, name, context={}):
        self.name = name
        self.context = context

    def __repr__(self):
        return self.__class__.__name__ + ': ' + self.name

    def register(self, element):
        if not isinstance(element, (Point, Segment)):
            raise Exception('element must be point, segment...')

        existing_ids = self.context.keys()
        exception_template = '''{} already existed, cannot overide
        it with another object, if you want to update an existing 
        element, use update(wip)'''

        element_info = (element.__class__.__name__, element)
        e_name = element.name
        e_alias = element.alias

        exception_msg = exception_template.format(e_name)

        if not e_name in existing_ids:
            self.context[e_name] = element_info
            element.hook_graph(self)
        else:
            raise Exception(exception_msg)

        if (not e_alias is None) and (not e_alias == e_name):
            if not e_alias in existing_ids:
                self.context[e_alias] = element_info
            else:
                raise Exception(exception_msg)

        if 'reversed_name' in element.__dict__.keys():
            e_rname = element.reversed_name
            if not e_rname in existing_ids:
                self.context[e_rname] = element_info
            else:
                raise Exception(exception_msg)
