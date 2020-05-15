from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce
from functools import reduce
import operator 

def addition(n): 
    return n + n 

def main():
    numbers = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
    result = map(addition, numbers)
    print(list(result))
    result2 = ft_map(addition, numbers)
    print(list(result2))

    result = filter(lambda x: x > 0, numbers)
    print(list(result))
    result2 = ft_filter(lambda x: x > 0, numbers)
    print(list(result2))

    result = reduce(lambda x, y: x+y, [1, 2, 3, 4, 5], 5)
    print(result)
    result2 = ft_reduce(lambda x, y: x+y, [1, 2, 3, 4, 5], 5)
    print(result2)
    lis = [ 1 , 3, 5, 6, 2, ] 
    print ("The sum of the list elements is : ",end="") 
    print (reduce(operator.add,lis)) 
    print ("The product of list elements is : ",end="") 
    print (reduce(operator.mul,lis, 20))
    print ("The concatenated product is : ",end="") 
    print (reduce(operator.add,["geeks","for","geeks"], "Hello"))

    print ("The sum of the list elements is : ",end="") 
    print (ft_reduce(operator.add,lis)) 
    print ("The product of list elements is : ",end="") 
    print (ft_reduce(operator.mul,lis, 20))
    print ("The concatenated product is : ",end="") 
    print (ft_reduce(operator.add,["geeks","for","geeks"], "Hello")) 

if __name__ == "__main__":
    main()