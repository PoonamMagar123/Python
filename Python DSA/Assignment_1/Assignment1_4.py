def prime_factor(nlist):
    prime = []
    for i in nlist:
        flag = 0
        if i==1:
            flag=1
        for j in range(2,i):
            if i%j == 0:
                flag = 1
                break
        if flag == 0:
            prime.append(i)            
    return prime

        
def main():
    
    Number = int(input("Enter a Number : "))  
    
    primelist = []
    
    for Num in range(Number):
        value = int(input())
        primelist.append(value) 
    
    Numlist = prime_factor(primelist)
    print("Prime Numbers are in list : ",Numlist)
    
if __name__ == "__main__":
    main()