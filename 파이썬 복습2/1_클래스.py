# 딕셔너리를 사용해 간단한 캐릭터 정보를 표현한 예시
hero = {
    "name": "lubi",
    "hp": 100,
    "mp": 100,
    "power": 30,
    "drop_rate": 0,
    "attack": lambda: f'{hero["power"]}에 파워로 공격하였습니다.',
}
print(hero["hp"])
print(hero["attack"]())

## 위 코드를 클로저로 구현한 것
def create_character(name, hp, mp, power):
    data = {"name": name, "hp": hp, "mp": mp, "power": power}
    def get_data(key):
        return data[key]
    def attack():
        return f"{get_data('power')}의 파워로 공격"
    return {"attack": attack}
hero = create_character("lubi", 100, 100, 30)
print(hero["attack"]())


# 인스턴스 변수 : 인스턴스 객체가 생성될 때 생성
## 클래스 변수 : 클래스가 메모리에 로드될 때 생성
## 인스턴스 변수는 self가 위치한 어디서나 선언 가능, 보통 __init__메서드 안에 선언
## __init__메서드 : 인스턴스 객체를 생성할 때 자동으로 실행
class Car:
    max_speed = 300
    def __init__(self, name): # self는 인스턴스 고유 영역
        self.name = name
    def start(self, speed): # self는 인스턴스 고유 영역
        self.speed = speed
        return f'{self.name}차가 {self.speed}의 속력으로 움직임'
model = Car('lubi')
print(model.name)
print(model.start(100))