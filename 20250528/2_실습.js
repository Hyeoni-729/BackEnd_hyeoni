console.log("준비");

setTimeout(() => {
  console.log("첫 번째 작업 완료");
}, 0);

console.log("시작");

setTimeout(() => {
  console.log("두 번째 작업 완료");
}, 50);

setTimeout(() => {
  console.log("모든 작업 끝");
}, 100);
