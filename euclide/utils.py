import yaml

from itertools import combinations

from .element.point import Point
from .element.segment import Segment
from .graph.graph2D import Graph2D


def find_longest_segment(segment_name):
    return segment_name[0] + segment_name[-1]

def graph2d_from_yaml(file_path, name='graph'):
    graph = Graph2D(name)
    with open(file_path) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    # If no relation field exists in yaml file, set initial state for relations
    try:
        relations = data['relations']
    except KeyError:
        relations = {'co_linear': []}

    try:
        co_linear = relations['co_linear']
    except KeyError:
        co_linear = relations['co_linear'] = []


    # If no explicit_info exists in yaml file, set initial state for explicit_info
    try:
        explicit_info = data['explicit_info']
    except KeyError:
        explicit_info = []

    # If no point exists in yaml file, skip registering points
    # Since teachers only need to specify a higer level of element and 
    # the program should handle the rest for them, this might occur often
    try:
        points = data['points']
        print('Registering points: ', points)
        for p in points:
            graph.add_point(p)
    except KeyError:
        print('points not defined in problem, skipping ...')

    # If no segment exists in yaml file, skip registering segments
    # The reason is elaborated above
    try:
        segments = data['segments']
        longest_segments = [find_longest_segment(s) for s in segments]
        # also if length of segment is gte 3, then it is becuase certain
        # poinits are co-linear
        co_linear += [s for s in segments if len(s) >= 3]
        print('Registering longest segments: ', longest_segments)
        for s in longest_segments:
            graph.add_segment(s)
    except KeyError:
        print('segments not defined in problem, skipping ...')

    # If no line exists in yaml file, skip registering lines
    # The reason is elaborated above
    try:
        lines = data['lines']
        print('Registering lines: ', lines)
        for l in lines:
            graph.add_line(l)
    except KeyError:
        print('lines not defined in problem, skipping ...')

    # If no angle exists in yaml file, skip registering angles
    # The reason is elaborated above
    try:
        angles = data['angles']
        print('Registering angles: ', angles)
        for a in angles:
            graph.add_angle(a)
    except KeyError:
        print('angles not defined in problem, skipping ...')

    # Identify angles from already known segments, must make sure
    # the segments registered are longest segment otherwise the program
    # may not work under certain circumstances, like angle D.
    for angle in graph.identify_angles():
        graph.add_angle(angle)

    # Merge co_linear from relations to graph.relations.co_linear
    try:
        colinear_segments = graph.relations['co_linear'] + co_linear
        colinear_segments = list(set(colinear_segments))
        graph.relations['co_linear'] = colinear_segments
        print('Registering co-linear segments: ', colinear_segments)
        for s in colinear_segments:
            combos = combinations(list(s), 2)
            for combo in combos:
                seg_name = "".join(combo)
                graph.add_segment(seg_name)
    except KeyError:
        print('Segments not defined in problem, skipping ...')

    # Since new segments are registered to registry, recompute the angles
    # in the graph
    for angle in graph.identify_angles():
        graph.add_angle(angle)

    # Registering alias for elements, if alias is not defined in template, skip
    # It is the one of the last two steps of getting information
    try:
        alias = data['alias']
        alias_name = [a['name'] for a in alias]
        print('Registering alias: {}'.format(alias_name))
        for alias_dict in alias:
            elem_type = alias_dict['type']
            name = alias_dict['name']
            elem_alias = alias_dict['alias']

            element = graph.get_element(elem_type, name)
            graph.alias_element(element, elem_alias)
    except KeyError:
        print('Alias not defined in problem, skipping ...')

    # Before we can go any further we need to add explicit information
    # to elements

    return graph
