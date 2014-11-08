__author__ = 'Fernando Morillo, Joschka Rick'

import math as m


def gauss(x, u, o):
    t1 = 1 / (m.sqrt(2*m.pi) * o)
    t2 = m.exp(-0.5 * (m.pow(x - u, 2)/m.pow(o, 2)))
    return t1 * t2


known = {'x1': 1, 'x2': 4, 'x3': 7, 'x4': 10,
         'z1': 6.5, 'z2': 4, 'z3': 2, 'z4': 12,
         'px1': 0.4, 'px2': 0.4, 'px3': 0.1, 'px4': 0.1}

# P(z1|xi)
r1 = gauss(known['x1'], known['z1'], 2) * known['px1']
r2 = gauss(known['x2'], known['z1'], 2) * known['px2']
r3 = gauss(known['x3'], known['z1'], 2) * known['px3']
r4 = gauss(known['x4'], known['z1'], 2) * known['px4']

sum_z1 = (r1 + r2 + r3 + r4)

print("-----------------------")
print("P(x1|z1)=", r1 / sum_z1)
print("P(x1|z2)=", r2 / sum_z1)
print("P(x1|z3)=", r3 / sum_z1)
print("P(x1|z4)=", r4 / sum_z1)

# P(z2|xi)
r1 = gauss(known['x1'], known['z2'], 2) * known['px1']
r2 = gauss(known['x2'], known['z2'], 2) * known['px2']
r3 = gauss(known['x3'], known['z2'], 2) * known['px3']
r4 = gauss(known['x4'], known['z2'], 2) * known['px4']

sum_z2 = (r1 + r2 + r3 + r4)

print("-----------------------")
print("P(x2|z1)=", r1 / sum_z2)
print("P(x2|z2)=", r2 / sum_z2)
print("P(x2|z3)=", r3 / sum_z2)
print("P(x2|z4)=", r4 / sum_z2)

# P(z3|xi)
r1 = gauss(known['x1'], known['z3'], 2) * known['px1']
r2 = gauss(known['x2'], known['z3'], 2) * known['px2']
r3 = gauss(known['x3'], known['z3'], 2) * known['px3']
r4 = gauss(known['x4'], known['z3'], 2) * known['px4']

sum_z3 = (r1 + r2 + r3 + r4)

print("-----------------------")
print("P(x3|z1)=", r1 / sum_z3)
print("P(x3|z2)=", r2 / sum_z3)
print("P(x3|z3)=", r3 / sum_z3)
print("P(x3|z4)=", r4 / sum_z3)

# P(z4|xi)
r1 = gauss(known['x1'], known['z4'], 2) * known['px1']
r2 = gauss(known['x2'], known['z4'], 2) * known['px2']
r3 = gauss(known['x3'], known['z4'], 2) * known['px3']
r4 = gauss(known['x4'], known['z4'], 2) * known['px4']

sum_z4 = (r1 + r2 + r3 + r4)

print("-----------------------")
print("P(x4|z1)=", r1 / sum_z4)
print("P(x4|z2)=", r2 / sum_z4)
print("P(x4|z3)=", r3 / sum_z4)
print("P(x4|z4)=", r4 / sum_z4)