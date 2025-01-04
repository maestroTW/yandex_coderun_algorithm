A = int(input())
B = int(input())
C = int(input())

def main(A, B, C):
    res = "YES"
    if (A + B <= C) or (A + C <= B) or (B + C <= A):
        res = "NO"
    return res
if __name__ == '__main__':
    print(main(A,B,C))
