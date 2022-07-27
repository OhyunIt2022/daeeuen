print("helloworld")
print("진행할 작업을 선택해주세요")
print("1.메모작성 2. 메모읽기")


option = input()

print(option)

if option =='1':
    newmemo = input("메모를 입력해주세요")
    print(newmemo)
    filename = 'memo.txt'
    f = open(filename,'a')
    f.write(newmemo)
    f.close()
    print("아직 구현")
elif option == '2':
    filename = 'memo2.txt'
    f=open(filename)
    memo = f.read()
    print(memo)
    f.close()
else:
    print("잘못입력했습니다")    
