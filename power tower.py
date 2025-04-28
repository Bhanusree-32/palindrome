def pt(a,n):
  if n==1:
    return a
  return a**pt(a,n-1)
print(pt(2,3))
