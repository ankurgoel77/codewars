# https://www.codewars.com/kata/5b98dfa088d44a8b000001c1

def get_volume(heightmap):
    rows = len(heightmap)
    cols = len(heightmap[0])

    visited = [[0 for j in range(0,cols)] for i in range(0,rows) ]
    print(visited)

    pass

heightmap = [
  [8, 8, 8, 8, 6, 6, 6, 6],
  [8, 0, 0, 8, 6, 0, 0, 6],
  [8, 0, 0, 8, 6, 0, 0, 6],
  [8, 8, 8, 8, 6, 6, 6, 0],
]

get_volume(heightmap)