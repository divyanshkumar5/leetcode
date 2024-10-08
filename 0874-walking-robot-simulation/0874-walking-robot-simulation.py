class Solution:
  def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
    ans = 0
    d = 0  # 0 := north, 1 := east, 2 := south, 3 := west
    x = 0  # the start x
    y = 0  # the start y
    obstaclesSet = {(x, y) for x, y in obstacles}

    for c in commands:
      if c == -1:
        d = (d + 1) % 4
      elif c == -2:
        d = (d + 3) % 4
      else:
        for _ in range(c):
          if (x + dirs[d], y + dirs[d + 1]) in obstaclesSet:
            break
          x += dirs[d]
          y += dirs[d + 1]

      ans = max(ans, x * x + y * y)

    return ans