def is_prime(x):
    y=0
    if x<=1:
        return False
    elif x == 2:
        return True
    elif x%2==0:
        return False
    else:
        root = int(x**.5)+2
        for i in xrange (2,root):
            if x%i==0:
                return False
                y=1
        if y==0:
            return True
