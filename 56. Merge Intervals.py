class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    Res= []
    s_Int = sorted(intervals)
    for I in s_Int:
      if not Res or Res[-1][1] < I[0]:
        Res.append(I)
      else:
        Res[-1][1] = max(Res[-1][1], I[1])
    return Res