def amazon(c):
    total =0 
    
    while c > 0 :
        digit = c%10
        c = c//10 

        if digit%2 == 0 :
            total += 2 

        else:
            total += 3
    


    return total

    
print(amazon(1239))