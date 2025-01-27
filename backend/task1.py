import sys

list = list(map(int, input().split()))

def main():
    list.sort()
    print(list[1])

if __name__ == '__main__':
    main()