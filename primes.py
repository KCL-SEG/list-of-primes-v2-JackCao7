"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    if number_of_primes <= 0:
        raise ValueError(f"Number of primes cannot be 0 or negative")
    
    elif number_of_primes == 1: 
        list.append(2)
    else:
        list.append(2)
        list.append(3)
        if number_of_primes > 2: 
            i=2                                     
            scan = 4
            while i < number_of_primes:
                div = 2
                while div < scan:   
                    if div == (scan-1):
                        list.append(scan)
                        i+=1
                        div+=1
                    elif not(scan%div==0):    
                        div+=1            
                    else:               
                        break
                scan+=1
    return list



#5%2, 5%3, 5%4 = append

#7%2, 7%3, 7%4, 7%5, 7%6 = append

#25%3 = next number

#i=2
#scan = 4
#div = 2
#while i < number_of_primes:
#
#   while div < scan:   
#       scan+=1
#       if y == (scan-1):
#           list.append(scan)
#           i+=1
#       elif not(scan%div==0):    
#           div+=1            
#       else:               
#           break
#   i+=1
#       
# 
#  