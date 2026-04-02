def isPalindrome(s: str)->bool:
	return s == s[::-1]


## two pointer

def isPal(s):
	n = len(s)
	l, r = 0, n-1
	while l<r:
		if s[l] != s[r]:
			return False
		l += 1
		r -= 1
	return True

