from itertools import combinations
from collections import Counter

from ..element import (
    Angle,
    Point,
    Segment,
    Line,
)
from ..validations import (
    point_validation,
    segment_validation
)


class BaseGraph(object):
    def __init__(self, name):
        self.name = name
        self.registry = {}
        self.relations = {'co_linear': []}

    def __repr__(self):
        return self.__class__.__name__ + ': ' + self.name

    def _register(self, element):
        if not isinstance(element, (Point, Segment, Line, Angle)):
            raise Exception('element must be point, segment...')

        existing_ids = self.registry.keys()
        warning_template = '{} {} already existed, cannot overide it with another object'

        e_name = element.name

        # register name
        key = (element.__class__.__name__, e_name)
        if key not in existing_ids:
            self.registry[key] = element
            element.hook_graph(self)
        else:
            print(warning_template.format(*key))

        # register reverse name
        if 'reversed_name' in element.__dict__.keys():
            e_rname = element.reversed_name
            key = (element.__class__.__name__, e_rname)
            if key not in existing_ids:
                self.registry[key] = element
            else:
                print(warning_template.format(*key))

        return key

    def _filter_registry_key(self, cls):
        elem_type = cls.__name__
        elems = (k[1] for k, v in self.registry.items() if k[0] == elem_type)
        return elems

    def _filter_registry_value(self, cls):
        elem_type = cls.__name__
        elems = (v.name for k, v in self.registry.items() if k[0] == elem_type)
        return elems

    def get_element(self, elem_type, name):
        key = (elem_type.capitalize(), name)
        try:
            return self.registry[key]
        except KeyError:
            return None

    def alias_element(self, element, alias):
        warning_template = '{} {} already existed, cannot overide it with another object'
        key = (element.__class__.__name__, alias)
        if key not in self.registry.keys():
            self.registry[key] = element
        else:
            print(warning_template.format(*key))
        return key


    def add_point(self, point_name):
        '''
        point_name: the name of a point to be created, e.g. A

        It is a helper function that deals with all the side effects of adding a point to the graph
        '''
        point = Point(point_name)
        self._register(point)

        return point

    def add_segment(self, segment_name):
        '''
        segment_name: the name of the segment defined in the problem
                      e.g. AB or a

        It is a helper function that deals with all the side effects of
        add a new segment to the graph
        '''
        segment = Segment(segment_name)
        self._register(segment)

        if len(segment_name) == 2:
            points_exists = set(self._filter_registry_key(Point))
            segment_endpoints = {segment_name[0], segment_name[1]}
            # If there exists certain point not in registry, register for them
            # and append points to segment instance
            for endpoint in segment_endpoints.difference(points_exists):
                edpt = self.add_point(endpoint)
                print('{} not found, registering...'.format(endpoint))
                segment.append_point(edpt)

            # Append points to segment instance
            for endpoint in segment_endpoints.intersection(points_exists):
                edpt = self.registry[('Point', endpoint)]
                segment.append_point(edpt)

        return segment

    def add_line(self, line_name):
        pass

    def add_angle(self, angle_name):
        '''
        angle_name: the name of the angle defined in the problem
                      e.g. ABC or A or 1

        It is a helper function that deals with all the side effects of
        add a new angle to the graph
        '''
        angle = Angle(angle_name)
        self._register(angle)

        if angle_name.isalpha():
            points_exists = set(self._filter_registry_key(Point))
            angle_point = set(angle_name)
            for pnt in angle_point.difference(points_exists):
                point = self.add_point(pnt)
                print('{} not found, registering...'.format(pnt))
                angle.append_point(point)

            for pnt in angle_point.intersection(points_exists):
                point = self.registry[('Point', pnt)]
                angle.append_point(point)

        if (angle_name.isalpha()) and (len(angle_name) == 3):
            segments_exists = set(self._filter_registry_key(Segment))
            segments = {angle_name[:2], angle_name[1:]}
            for seg in segments.difference(segments_exists):
                print(seg)
                segment = self.add_segment(seg)
                print('{} not found, registering...'.format(seg))
                angle.append_segment(segment)

            for seg in segments.intersection(segments_exists):
                segment = self.registry[('Segment', seg)]
                angle.append_segment(segment)

        return angle

    def identify_angles(self):
        '''
        After segments are registered, angles could be identified from segments in the graph
        '''
        segments = set(self._filter_registry_value(Segment))
        combos = combinations(segments, 2)
        angle_list = []
        angle_points = []

        for combo in combos:
            seg_1, seg_2 = combo
            seg_1_points = set(seg_1)
            seg_2_points = set(seg_2)
            intersection = seg_1_points.intersection(seg_2_points)

            if len(intersection) == 1:
                angle_point = intersection.pop()
                point_1 = seg_1.replace(angle_point, '')
                point_2 = seg_2.replace(angle_point, '')

                angle_name = point_1 + angle_point + point_2
                angle_name_set = set(angle_name)

                # if co_linear information are not set properly
                # co_linear angles may be accidentally identified
                # right now, a 180 angle is ignored here
                if len(self.relations['co_linear']) == 0:
                    angle_points.append(angle_point)
                    angle_list.append(angle_name)
                else:
                    co_linear_set = [set(elem)
                                     for elem in self.relations['co_linear']]
                    is_valid_name = not any(
                        angle_name_set == elem for elem in co_linear_set)

                    if is_valid_name:
                        angle_points.append(angle_point)
                        angle_list.append(angle_name)
                    else:
                        print(
                            'Dropping angle {}, because of co_linearity'.format(angle_name))

        angle_points_counter = Counter(angle_points)
        single_angle_points = [
            k for k, v in angle_points_counter.items() if v == 1]

        angle_list += single_angle_points

        # remove already identified angles in registry
        existing_angles = set(self._filter_registry_key(Angle))
        angle_set = set(angle_list)

        angle_set = angle_set.difference(existing_angles)

        return angle_list
