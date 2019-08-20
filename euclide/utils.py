import yaml

from itertools import combinations

from .element.point import Point
from .element.segment import Segment
from .graph.graph2D import Graph2D


def graph2d_from_yaml(file_path, name='graph'):
    with open(file_path) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    relations = data['relations']
    alias_map = data['alias_map']
    explicit_info = data['explicit_info']

    graph = Graph2D(name)

    try:
        points = data['points']
        print('Registering points: ', points)
        for p in points:
            graph.add_point(p)
    except KeyError:
        print('points not defined in problem, skipping ...')

    try:
        segments = data['segments']
        print('Registering segments: ', segments)
        for s in segments:
            graph.add_segment(s)
    except KeyError:
        print('segments not defined in problem, skipping ...')

    try:
        lines = data['lines']
        print('Registering lines: ', lines)
        for l in lines:
            graph.add_line(l)
    except KeyError:
        print('lines not defined in problem, skipping ...')

    try:
        angles = data['angles']
        print('Registering angles: ', angles)
        for a in angles:
            graph.add_angle(a)
    except KeyError:
        print('angles not defined in problem, skipping ...')

    for angle in graph.identify_angles():
        graph.add_angle(angle)

    try:
        segments = data['co_linear']
        print('Registering co-linear segments: ', segments)
        for s in segments:
            combos = combinations(list(s), 2)
            for combo in combos:
                seg_name = "".join(combo)
                graph.add_segment(seg_name)
        graph.relation['co_linear'] = segments
    except KeyError:
        print('segments not defined in problem, skipping ...')

    for angle in graph.identify_angles():
        graph.add_angle(angle)

    return graph
