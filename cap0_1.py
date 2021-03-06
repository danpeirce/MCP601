# C315C104M5U5TA7301  0.1 µF capacitor
# fits in     cube([3.81, 2.54, 3.14 + 1.52])

from solid import *

def cap100nf():
    SEGMENTS = 50
    inch = 25.4
    rad = 0.51/2
    boxx = 3.81
    boxy = 2.54
    boxz_3 = 3.14+1.52-boxy/2
    boxz_2 = 1.52 
    lead_offset1 = (boxx - inch*0.1)/2
    
    a0 = translate([boxx/2, boxy/2, boxz_3])(scale([boxx/boxy, 1, 1/2] )(sphere(d=boxy, segments = 50)))
    a2 = translate([boxx/2, boxy/2, boxz_2])(scale([boxx/boxy, 1, 1/2] )(sphere(d=boxy, segments = 50)))
    a3 = hull()(a0,a2)
    c3 = translate([lead_offset1, boxy/2, 0.333*boxz_2])(cylinder(r=lead_offset1*0.6, h=rad, segments = 50))
    c4 = translate([lead_offset1+0.1*inch, boxy/2, 0.333*boxz_2])(cylinder(r=lead_offset1*0.6, h=rad, segments = 50))
    a4 = hull()(a3,c3)
    a5 = hull()(a3,c4)
    c1 = translate([lead_offset1, boxy/2, 0])(cylinder(r1=rad, r2=lead_offset1, h=boxz_2, segments = 50))
    c2 = translate([lead_offset1+0.1*inch, boxy/2, 0])(cylinder(r1=rad, r2=lead_offset1, h=boxz_2, segments = 50))
    a1 = translate([0.5*inch,0.43*inch,9])(rotate([0,0,90]) (a4+a5+c1+c2))
    return a1


if __name__ == '__main__':
    a1 = cap100nf()
    file_out = scad_render_to_file(a1, "cap0_1.scad", include_orig_code=True)

	