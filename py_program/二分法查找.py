def search(sequence,number,lower,upper):
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower+upper)//2
        if number>sequence[middle]:
            return search(sequence,number,middle+1,upper)
        else:
            return search(sequence,number,lower,middle)
sequence=[0,1,2,3,4,5,6,7,8,9]
number=2
print(search(sequence,number,0,9))
