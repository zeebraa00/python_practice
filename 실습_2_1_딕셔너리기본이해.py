# 파이썬 2일차

def get_order() : # 주문받기함수
    order = input("메뉴를 입력해주세요: ")
    if order in cafe_menu :
        count = int(input("수량을 입력해 주세요: "))
        print("주문하신 %s %d잔은 %d원입니다."%(order, count, cafe_menu[order]*count))
    else :
        print("%s는 메뉴에 없습니다."%(order))
        get_order()

cafe_menu = {"아메리카노":2000,
             "카푸치노":3500,
             "카페라테":3500,
             "핫초코":3000}

print(cafe_menu) # 메뉴출력

get_order() # 주문받기함수 실행
