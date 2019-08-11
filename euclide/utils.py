import yaml


def graph2d_from_yaml(file_obj):
    data = yaml.load(file_obj)
    points = data['points']
    segments = data['segments']
    relations = data['relations']
    alias_map = data['alias_map']
    explicit_info = data['explicit_info']
