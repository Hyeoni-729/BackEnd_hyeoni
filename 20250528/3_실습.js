function 작업A() {
  console.log("작업A 시작");
  setTimeout(() => {
      console.log("작업A 완료");
  }, 150);
}

function 작업B() {
  console.log("작업B 시작");
  setTimeout(() => {
      console.log("작업B 완료");
  }, 100);
}

console.log("프로그램 시작");
작업A();
작업B();
console.log("프로그램 끝");