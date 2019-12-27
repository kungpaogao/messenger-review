# these do the same thing

s = "Some Name"

i0 = s.split(" ")[0][0]+s.split(" ")[1][0]
i1 = "".join(list(map(lambda s: s[0], s.split(" "))))
i2 = "".join([name[0] for name in s.split(" ")])
