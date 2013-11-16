import numpy

def create_line_segment(node_a, node_b):
    return [node_a.point(), node_b.point()]

def distance_between(node_a, node_b):
    point_a = node_a.point()
    point_b = node_b.point()

    return numpy.linalg.norm(point_a - point_b)

def intersect(line_segment, polygons):
    for polygon in polygons:
        if _intersect(line_segment, polygons):
            return True
    return False

def _intersect(line_segment, polygon):
    for edge in polygon.get_edges():
        t_value = _compute_t_value(line_segment, edge)
        if t_value >= 0 and t_value <= 1:
            return True

    return False

def _compute_t_value(intersector, intersectee):
    intersectee_dir = intersectee[1] - intersectee[0]
    normal = numpy.array([intersectee_dir[1], -intersectee_dir[0]])

    A = intersector[0]
    B = intersector[1]
    P = intersectee[0]

    print 'A: {}'.format(A)
    print 'B: {}'.format(B)
    print 'P: {}'.format(P)
    print 'normal: {}'.format(normal)

    return (A - P).dot(normal) / float((A - B).dot(normal))