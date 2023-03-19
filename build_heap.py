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
    v = input()
    if v == "I":
        n = int(input()) 
        assert 1<=n<=100000,"n out of bounds"
        data = list(map(int, input().split()))
        assert len(data) == n
    if v == "F":
        file_name=input()
        with open(file_name, 'r') as file:
            content = file.read()
            data=list(map(int,content.split()))
    swaps = build_heap(data)
    print(len(swaps))
    if v== "I":
        for i, j in swaps:
            print(i, j)


if __name__ == "__main__":
    main()
