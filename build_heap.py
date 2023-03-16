def build_heap(data):
    swaps = []
    sorted = False
    i=1
    j=2
    n=len(data)
    while sorted == False :
        while j<=i*2+1:
            if data[i-1]<data[j-1]:
                if j<n:
                    j+=1
                else:
                    sorted= True
                    break
                
            elif data[i-1]>data[j-1]:
                k=data[i-1]
                data[i-1]=data[j-1]
                data[j-1]=k
                swaps.append((i,j))
                i=1
                j=2
        if j==n:
            sorted= True
            break
        i=i+1
        j=i*2

    return swaps

def main():  
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    
    # input from keyboard
    n = int(input()) 
    assert 1<=n<=100000,"n out of bounds"
    data = list(map(int, input().split()))
    assert len(data) == n
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
