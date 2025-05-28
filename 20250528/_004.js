const user = {};
function setUser(callback) {
  setTimeout(() => {
    user.name = "luvi";
    user.age = 20;
    callback(user);
  }, 0);
}

function roleCheck(user, callback) {
  setTimeout(() => {
    if (user.age >= 20) {
      user.role = "성인";
    } else {
      user.role = "학생";
    }
    callback(user);
  }, 1000);
}

function printUser(user) {
  console.log(user);
}

setUser((user) => roleCheck(user, printUser));


// 콜백 지옥
func1(function (result1) {
  func2(result1, function(result2){
    func3(result2, function(result3){
      //계속되는 중첩...
    })
  })
});
