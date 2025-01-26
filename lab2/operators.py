#Python Arithmetic Operators:

"""
Operator 	Name	Example	
+	Addition	    x + y	
-	Subtraction	    x - y	
*	Multiplication	x * y	
/	Division	    x / y	
%	Modulus	        x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y   

"""

#Python Assignment Operators:
"""
Operator	Example	   Same As	
=	        x = 5	    x = 5	
+=	        x += 3	    x = x + 3	
-=	        x -= 3	    x = x - 3	
*=	        x *= 3	    x = x * 3	
/=	        x /= 3	    x = x / 3	
%=	        x %= 3	    x = x % 3	
//=	        x //= 3	    x = x // 3	
**=	        x **= 3	    x = x ** 3	
&=	        x &= 3	    x = x & 3	
|=	        x |= 3	    x = x | 3	
^=	        x ^= 3	    x = x ^ 3	
>>=     	x >>= 3	    x = x >> 3	
<<=	        x <<= 3	    x = x << 3	
:=	        print(x := 3)	x = 3
print(x)

"""
#Python Comparison Operators:
"""
Operator	Name	Example	Try it
==	        Equal	x == y	
!=	        Not equal	x != y	
>	        Greater than	x > y	
<	        Less than	x < y	
>=	        Greater than or equal to	x >= y	
<=	        Less than or equal to	x <= y

"""
# Python Logical Operators:
"""
Operator	Description	    Example
and 	Returns True if both statements are true	              x < 5 and  x < 10	
or	    Returns True if one of the statements is true	          x < 5 or x < 4	
not	    Reverse the result, returns False if the result is true	  not(x < 5 and x < 10)
"""

#Python Identity Operators:
"""
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x

print(x is y)
# returns False because x is not the same object as y,
even if they have the same content.

print(x == y)
# to demonstrate the difference betweeen "is" and "==": 
this comparison returns True because x is equal to y.


"""