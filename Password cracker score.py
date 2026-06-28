def password_score(n):

    sum_even = 0 
    sum_odd = 0 

    while n > 0 :
        digit = n%10
        n = n//10 

        if digit%2 == 0 :
            sum_even = sum_even + 2


        elif digit%2 != 0:
            sum_odd = sum_odd + 3

    total = sum_even + sum_odd 
    return total


print(password_score(111))






    