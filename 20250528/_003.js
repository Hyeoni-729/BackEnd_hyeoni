// 콜백함수 : 비동기 함수를 동기적으로 바꾼다
const user = {};
function setUser(callback) {
  setTimeout(() => {
    user.name = "luvi";
    callback(user);
  }, 0);
}

function printUser(user) {
  console.log(user);
}

setUser(printUser);
// 이렇게도 쓸 수 있음
// setUser((user) => console.log(user));
