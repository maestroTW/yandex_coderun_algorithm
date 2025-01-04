list = list(map(int, input().split()))

def main(list):
    res = 0
    for i in range(1, len(list)-1):
        if list[i] > list[i-1] and list[i] > list[i+1]:
            res += 1
        else:
            continue
    return res

if __name__ == '__main__':
    print(main(list))