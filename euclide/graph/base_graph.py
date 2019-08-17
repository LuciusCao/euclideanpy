from ..element.point import Point
from ..element.segment import Segment
from ..element.line import Line
from ..validations import (
    point_validation,
    segment_validation
)


class BaseGraph(object):
    def __init__(self, name, registry={}):
        self.name = name
        self.registry = registry

    def __repr__(self):
        return self.__class__.__name__ + ': ' + self.name

    def _register(self, element):
        if not isinstance(element, (Point, Segment, Line)):
            raise Exception('element must be point, segment...')

        existing_ids = self.registry.keys()
        exception_template = '{} already existed, cannot overide \
                              it with another object, if you want to update \
                              an existing element, use update(wip)'

        e_name = element.name
        e_alias = element.alias

        exception_msg = exception_template.format(e_name)

        if not e_name in existing_ids:
            key = (element.__class__.__name__, e_name)
            self.registry[key] = element
            element._hook_graph(self)
        else:
            raise Exception(exception_msg)

        if (not e_alias is None) and (not e_alias == e_name):
            if not e_alias in existing_ids:
                key = (element.__class__.__name__, e_alias)
                self.registry[key] = element
            else:
                raise Exception(exception_msg)

        if 'reversed_name' in element.__dict__.keys():
            e_rname = element.reversed_name
            if not e_rname in existing_ids:
                key = (element.__class__.__name__, e_rname)
                self.registry[key] = element
            else:
                raise Exception(exception_msg)

    def compute_graph(self):
        pass

    def add_point(self, point_name):
        '''
        point_name: the name of a point to be created, e.g. A
        '''
        _ = point_validation(point_name)
        point = Point(point_name)
        self._register(point)

    def add_segment(self, segment_name):
        '''
        segment_name: the name of the segment defined in the problem
                      e.g. AB or a
        '''
        _ = segment_validation(segment_name)

        if len(segment_name) == 2:
            points = (v for k, v in self.registry.items() if k[0] == 'Point')
            points_map = {p.name: p for p in points}

            endpoints = [segment_name[0], segment_name[1]]
            endpoints_exists = [edpt in points_map.keys()
                                for edpt in endpoints]

            if all(endpoints_exists):
                segment = Segment(segment_name)
                self._register(segment)

            else:
                raise Exception('Segments contains undefined points in graph')

        if len(segment_name) == 1:
            segment = Segment(segment_name)
            self._register(segment)

    def add_line(self, line_name):
        '''
        line_name: the name of the line defined in the problem e.g. AB
        '''
        points = (v for k, v in self.registry.items() if k[0] == 'Point')
        points_map = {p.name: p for p in points}

        endpoints = [line_name[0], line_name[1]]
        endpoints_exists = [edpt in points_map.keys() for edpt in endpoints]

        if all(endpoints_exists):
            tuple_of_points = tuple([points_map[edpt] for edpt in endpoints])
            line = Line(tuple_of_points)
            self._register(line)

        else:
            raise Exception('Line contains undefined points')
