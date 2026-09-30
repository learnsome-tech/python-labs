import json
def  total( prices,tax = 0.08 ):
    subtotal=sum( prices )
    return subtotal*(1+tax)
print( total([1.50,2.25]) )
