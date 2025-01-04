x,y,z = map(int, input().split(" "))
N = set(map(int, input()))

def main(x,y,z,N):
    res = 0
    for i in N:
        if i not in {x,y,z}:
            res += 1
    return res
if __name__ == '__main__':
    print(main(x,y,z,N))
