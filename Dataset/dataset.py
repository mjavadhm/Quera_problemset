def get_dataset(n):
    yon = {}
    for i in range(n):
        x = str(input()).split()
        yon[x[0]] = x[1]
    return yon

def get_string():
    x = str(input())
    return x

def check(yon,string):
    ans = ''
    if string in yon:
        ans = yon[string]
    else:
        ans = 'Unknown'
    return ans

def get_check(q,yon):
    x =[]
    for i in range(q):
        x.append(check(yon,get_string()))
    for j in range(q):
        print(x[j])
        
def main():
    inp = str(input())
    spilted = inp.split()
    n = int(spilted[0])
    q = int(spilted[1])
    l = int(spilted[2])
    yon = get_dataset(n)
    get_check(q,yon)
    
    
main()
