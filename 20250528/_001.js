// 동기적으로 동작하는 코드 : 순차적으로 처리하는 방식
console.log("hello");
console.log("world");

// 비동기적으로 동작하는 코드 : setTimeout
// setTimeout(() => {
//   console.log("hello");
// }, 1000); // 1초 후 실행
// console.log("world");

// setTimeout(() => {
//   console.log("hello");
// }, 0);
// console.log("world");

// 콜 스택 처리 과정
const 참깨빵 = () => {
  console.log("Call 참깨빵");
  순쇠고기패티();
  console.log("End 참깨빵");
};
const 순쇠고기패티 = () => {
  console.log("Call 순쇠고기패티");
  특별한소스();
  console.log("End 순쇠고기패티");
};
const 특별한소스 = () => {
  console.log("Call 특별한소스");
  console.log("End 특별한소스");
};
참깨빵();
console.log("---함수 호출 종료---");
