// 1단계: 기본 주문 처리

// 주문접수(음식명, 고객명, 콜백함수) 함수 구현
// 1초 후 "주문이 접수되었습니다" 메시지 출력
// 완료 후 콜백 함수 실행

// 2단계: 음식 준비

// 음식준비(음식명, 콜백함수) 함수 구현
// 2초 소요, 준비 완료 메시지 출력
// 완료 후 콜백 함수 실행

// 3단계: 배달 시작

// 배달시작(음식명, 주소, 콜백함수) 함수 구현
// 3초 소요, 배달 완료 메시지 출력
// 완료 후 콜백 함수 실행

// 4단계: 전체 과정 연결

// 위 3단계를 순서대로 실행하는 코드 작성
// "피자", "홍길동", "서울시 강남구"로 테스트
// 마지막에 "배달 완료!" 메시지 출력

// function order(food, name, callback){
//   setTimeout(() => {
//     console.log(`${food} 주문이 접수되었습니다.`);
//     callback();
//   }, 1000);
// };

// function ready(food,callback) {
//   setTimeout(() => {
//     console.log(`${food} 준비가 완료되었습니다.`);
//     callback();
//   }, 2000);
// };

// function deli(food, address, callback){
//   setTimeout(() => {
//     console.log(`${address}로 배달을 시작합니다.`);
//     callback();
//   }, 3000);
// };

// order('피자', '홍길동', function() {
//   ready('피자', function() {
//     deli('피자', '서울시 강남구', function() {
//       console.log('배달이 완료되었습니다.');
//       console.log('배달 완료!');
//     })
//   })
// })

// 강사님 풀이
function 주문접수(음식명, callback) {
  console.log(`${음식명} 주문이 접수되었습니다.`);
  setTimeout(() => {
    callback(음식명);
  }, 1000);
}

function 음식준비(음식명, callback) {
  console.log(`${음식명} 준비가 완료되었습니다.`);
  setTimeout(() => {
    callback();
  }, 2000);
}

function 배달시작(주소, callback) {
  console.log(`${주소}로 배달을 시작합니다.`);
  setTimeout(() => {
    console.log("배달이 완료되었습니다.");
    callback();
  }, 3000);
}

주문접수("피자", (음식명) => {
  음식준비(음식명, () => {
    배달시작("서울시 강남구", () => {
      console.log("배달 완료!");
    });
  });
});
