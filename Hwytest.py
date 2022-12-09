highway = int(input("HWY #?  "))


if highway == 0:
    print("not a valid highway.")
elif highway < 100:
    print("Primary Highway")
    if highway % 2 == 0:
        print("highway", highway, "runs east/west")
    else:
        print("highway", highway, "runs north/south")
