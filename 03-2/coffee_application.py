# coffee 실습해보기

americano = 500
latte = 1000

while True:
    money = int(input("돈을 넣어 주세요: "))
    """
    if 500 <= money < 1000:
        print("아메리카노를 줍니다.")
    elif money >= 1000:
        print("라떼를 줍니다.")
    """
    if money == americano:
        print("아메리카노를 줍니다.")
    elif money == latte:
        print("라테를 줍니다.")

    elif money > latte and money % latte == 0:
        print("라테 %d개를 줍니다." % (money / latte))

    elif americano < money < latte:
        print("아메리카노와 거스름돈 %d원을 줍니다." % (money - americano))
    elif money > latte and money % latte != 0:
        print("라테 %d개와 거스름돈 %d원을 줍니다." % (money / latte, money % latte))

