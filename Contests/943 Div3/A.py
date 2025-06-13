def gcd(a, b):
    
    while b:
        a, b = b, a % b
    return a

def find_ans(x):
    max1 = -1
    max2 = -1

    
    for y in range(1, x):
        
            v = gcd(x, y)
            
            vy= v + y
            
            if v + y > max1:
                max1 = v+y
                max2 = y

    return max2

for _ in range(int(input())):
    n = int(input())
    print(find_ans(n))