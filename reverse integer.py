def reverse_integer(x):
        sign = -1 if x < 0 else 1
        x *= sign

        # Remove leading zero in the reversed integer
        while x:
            if x % 10 == 0:
                x /= 10
            else:
                break
        
        # string manipulation
        x = str(round(x))
        lst = list(x)  # list('234') returns ['2', '3', '4']
        lst.reverse()
        x = "".join(lst)
        
        x = int(x)
        
        return sign*x
    
print(reverse_integer(1534236469))

