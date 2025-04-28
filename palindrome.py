def is_palindrome(s):
  if len(s)>=1:
    return True
  return check_palindrome(s,0,len(s)-1)
def check_palindrome(s,start,end):
  if start>=end:
    return True
  if s[start]!=s[end]:
    return False
  return is_plaindrome(s[start+1:end])
print(is_palindrome("rececar"))
print(is_palindrome("hello"))
print(is_palindrome("level"))
