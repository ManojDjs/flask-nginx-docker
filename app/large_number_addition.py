# Only valid with positive integers
# Optimum for Database identifiers.


# Function for summing of larger numbers
def findSum(str1, str2):

    # Set temporal structures
    __s1 = str(str1)
    __s2 = str(str2)

    # Check length of both str
    if len(__s1) > len(__s2):

        # Interchange values
        __tmp = __s1
        __s1 = __s2
        __s2 = __tmp

    # Structure for result
    __r = ""
    __c = 0

    # Calculate length
    __n1 = len(__s1)
    __n2 = len(__s2)

    # Traverse from end of both strings
    for i in range(__n1 - 1, -1, -1):

        # Compute sum of current digits & carry
        __s = (
            (ord(__s1[i]) - ord('0')) + 
            int((ord(__s2[i + (__n2 - __n1)]) - ord('0'))) + 
            __c
        )
        __r += str(__s % 10)
        __c = __s // 10

    # Add remaining digits
    for i in range(__n2 - __n1 - 1, -1, -1):
        __s = ((ord(__s2[i]) - ord('0')) + __c)
        __r += str(__s % 10)
        __c = __s // 10

    # Add remaining carry
    if __c:
        __r += str(__c)

    # reverse resultant string
    return __r[::-1]
