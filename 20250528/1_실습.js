console.log("시작");
setTimeout(() => {
  console.log("타이머 A");
}, 100);
setTimeout(() => {
  console.log("타이머 B");
}, 50);
console.log("중간");
setTimeout(() => {
  console.log("타이머 C");
}, 0);
