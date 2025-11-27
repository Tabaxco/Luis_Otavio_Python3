### def soma (x, y, z=0):
   ## if z:
      ##  print(f'{x=} {y=} {z=}', x + +z)
   ## else:
       ## print(f'{x=} {y=}', x +y)


def sum(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y +z)
    else:
        print(f'{x=} {y=}', x + y)

sum(1, 2)