
import math
m,n,a = map(int,input().split())
horizontal = math.ceil(m/a)
vertical = math.ceil(n/a)
c=horizontal*vertical
print(c)