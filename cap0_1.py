# C315C104M5U5TA7301  0.1 µF capacitor
# fits in     cube([3.81, 2.54, 3.14 + 1.52])
import sys
from math import cos, radians, sin

from euclid3 import Point3

from solid import *
from solid.utils import extrude_along_path

SEGMENTS = 50
inch = 25.4
rad = 0.51/2
boxx = 3.81
boxy = 2.54
boxz_3 = 3.14+1.52-boxy/2
boxz_2 = 1.52 
lead_offset1 = (boxx - inch*0.1)/2

def path1():
    outline = [Point3(boxx/2, boxy/2, boxz_2), 
        Point3(boxx/2, boxy/2, boxz_3)]
    return outline

def path2():
    outline = [Point3(boxx/2, boxy/2, boxz_3), 
        Point3(boxx/2, boxy/2, boxz_3+rad)]
    return outline

def body1(num_points=50):
    star_pts = []
    for i in range(2 * num_points):
        angle = radians(360 / (2 * num_points) * i)
        star_pts.append(Point3(boxx/2 * cos(angle), boxy/2 * sin(angle), 0))
    return star_pts

def extrude_path1():
    shape = body1()
    path = path1()

    extruded = extrude_along_path(shape_pts=shape, path_pts=path)

    return extruded

def extrude_path2():
    shape = body2()
    path = path2()

    extruded = extrude_along_path(shape_pts=shape, path_pts=path)

    return extruded

if __name__ == '__main__':
    a0 = translate([boxx/2, boxy/2, boxz_3])(scale([boxx/boxy, 1, 1/2] )(sphere(d=boxy, segments = 50)))
    a2 = translate([boxx/2, boxy/2, boxz_2])(scale([boxx/boxy, 1, 1/2] )(sphere(d=boxy, segments = 50)))
    c1 = translate([lead_offset1, boxy/2, 0])(cylinder(r1=rad, r2=lead_offset1, h=boxz_2, segments = 50))
    c2 = translate([lead_offset1+0.1*inch, boxy/2, 0])(cylinder(r1=rad, r2=lead_offset1, h=boxz_2, segments = 50))
    a1 = extrude_path1() + a0 + a2 + c1 + c2
    # translate([boxx/2, boxy/2, boxz_3])(scale([boxx/boxy, 1, 1/2] )(sphere(d=boxy, segments = 50)))

    file_out = scad_render_to_file(a1, "cap0_1.scad", include_orig_code=True)

	