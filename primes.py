"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    if number_of_primes <= 0:
        raise ValueError("Number of primes cannot be 0 or negative")
    else:
        list.append(2)
        if number_of_primes > 1: 
            i=1                                     
            scan = 3
            while i < number_of_primes:
                div = 2
                while (div < scan):   
                    if div == (scan-1):
                        list.append(scan)
                        i+=1            
                    elif not(scan%div==0):
                        pass
                    else:               
                        break  
                    div+=1          
                scan+=2
    return list