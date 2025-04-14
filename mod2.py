def add(a,b):
    return a+b

def sub(a,b):
    return a-b

#스스로 호출시에만 생성 import 됐을땐 실행안됨됨
if __name__ == "__main__":
    
    print(add(1,4))
    print(sub(4,2))

# print(add(1,4))
# print(sub(4,2))