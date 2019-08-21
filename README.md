# euclidepy
A package to describe and solve for geometry problems

## Sample Problems
A geometry problem is defined by `yaml` using the following fields `points`, `segments`, `relations`, `alias`, `explicit_info`. Where `points` is a list of points that are registered in a single graph. `segments` are list of segments connected by points registered. And `relations` are extra information about the position of elemnts on the graph, e.g. three points are co_linear etc. The first three fields together describe the shape of the graph. While `alias_map` is used to create alias for some elements when they are registered to a graph, e.g. angle ABC can be also written as angle 1, and students might use that as an infomation in solving the questions. `explicit_info` is used to help the graph to store information provided by the problem itself. All examples goes to `./examples` directory.
