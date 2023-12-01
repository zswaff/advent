with open("inp.txt") as fin:
    w1s, w2s = [e.strip() for e in fin.readlines()]

o = (0, 0, 0)


# part 1
def m_dist(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])


d_dict = {"U": (0, 1), "R": (1, 0), "D": (0, -1), "L": (-1, 0)}


def to_coords(s):
    res = [o]
    for e in s.split(","):
        d, m = e[0], int(e[1:])
        (
            xm,
            ym,
        ) = d_dict[d]
        res.append((res[-1][0] + m * xm, res[-1][1] + m * ym, res[-1][2] + m))
    return res


w1c = to_coords(w1s)
w2c = to_coords(w2s)


def segs_cross(s1, e1, s2, e2):
    dx1, dy1 = s1[0] - e1[0], s1[1] - e1[1]
    dx2, dy2 = s2[0] - e2[0], s2[1] - e2[1]
    if dx1 * dx2 != 0 or dy1 * dy2 != 0:
        return None

    if dy1 == 0:
        hs, he, vs, ve = s1, e1, s2, e2
    else:
        hs, he, vs, ve = s2, e2, s1, e1

    hy = hs[1]
    hx_min, hx_max = min(hs[0], he[0]), max(hs[0], he[0])
    vx = vs[0]
    vy_min, vy_max = min(vs[1], ve[1]), max(vs[1], ve[1])

    if hx_min <= vx <= hx_max and vy_min <= hy <= vy_max:
        res = vx, hy
        return vx, hy, s1[2] + s2[2] + m_dist(s1, res) + m_dist(s2, res)
    return None


def list_crosses(w1c, w2c):
    res = []
    for i in range(1, len(w1c)):
        for j in range(1, len(w2c)):
            cross = segs_cross(w1c[i - 1], w1c[i], w2c[j - 1], w2c[j])
            if cross is not None:
                res.append(cross)
    return res


crosses = list_crosses(w1c, w2c)

print(min(m_dist(o, e) for e in crosses))


# part 2
print(min(e[2] for e in crosses))
