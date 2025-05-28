"""
1번 : 간단한 은행 계좌 클래스
BankAccount 클래스를 만들어서 다음 기능을 구현하세요.
* 조건
생성 시 이름과 초기 잔액을 입력받음,
deposit(amount) 메서드: 잔액에 돈을 입금,
withdraw(amount) 메서드: 잔액에서 돈을 출금
출금하려는 금액이 잔액보다 많으면 "잔액 부족" 출력,
check_balance() 메서드: 현재 잔액 출력,
"""
class BankAccount:
    def __init__(self, name, money):
        """
        은행 계좌 생성
        name : 계좌 소유자 이름
        money : 초기 잔액
        """
        self.name = name
        self.money = money

    def deposit(self, inamount):
        """
        입금 메서드
        amount : 입금할 금액
        """
        self.money += inamount

    def withdraw(self, outamount):
        """
        출금 메서드
        amount : 출금할 금액
        """
        if outamount > self.money:
            print("잔액 부족")
        else:
            self.money -= outamount

    def check_balance(self):
        """
        현재 잔액 메서드
        """
        print(f"현재 잔액은 {self.money}원")


acc = BankAccount("luvi", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.check_balance()  # 출력: 현재 잔액은 1200원입니다.
acc.withdraw(2000)  # 출력: 잔액 부족


"""
2번 : 온라인 쇼핑 장바구니 클래스
ShoppingCart 클래스를 만들어 다음 기능을 구현하세요.
* 조건
생성 시 빈 장바구니를 리스트로 준비,
add_item(item_name, price) 메서드: 장바구니에 항목 추가,
total_price() 메서드: 장바구니 안 항목들의 총 가격 출력,
show_items() 메서드: 장바구니에 들어간 물건 이름과 가격 출력
"""
class ShoppingCart:
    def __init__(self):
        """
        쇼핑 장바구니 생성
        빈 리스트로 장바구니 초기화
        """
        self.cart = []

    def add_item(self, item_name, price):
        """
        장바구니에 항목 추가
        item_name : 상품명
        price : 가격
        """
        item = {"name": item_name, "price": price}
        self.cart.append(item)

    def show_items(self):
        """
        장바구니에 들어간 물건 이름과 가격 출력
        """
        for item in self.cart:
            print(f"{item['name']} : {item['price']}원")

    def total_price(self):
        """
        장바구니 안 항목들의 총 가격 출력
        """
        total = 0
        for item in self.cart:
            total += item["price"]
        print(f"총 가격은 {total}원")


cart = ShoppingCart()
cart.add_item("사과", 1000)
cart.add_item("바나나", 1500)
cart.show_items()
# 사과: 1000원
# 바나나: 1500원

cart.total_price()
# 총 가격은 2500원입니다.
