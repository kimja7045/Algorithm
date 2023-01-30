// 프로그래머스, level2, 문제 설명
// 피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.

// 예를들어

// F(2) = F(0) + F(1) = 0 + 1 = 1
// F(3) = F(1) + F(2) = 1 + 1 = 2
// F(4) = F(2) + F(3) = 1 + 2 = 3
// F(5) = F(3) + F(4) = 2 + 3 = 5
// 와 같이 이어집니다.

// 2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.

// 제한 사항
// n은 2 이상 100,000 이하인 자연수입니다.

// 입출력 예
// n	return
// 3	2
// 5	5

// before
function fibonacci(arr, n) {
  if (arr[n]) {
    return arr[n];
  } else if (n <= 1) {
    return n;
  } else {
    arr[n] =
      (fibonacci(arr, n - 1) % 1234567) + (fibonacci(arr, n - 2) % 1234567);
    return arr[n] % 1234567;
  }
}

function solution(n) {
  let arr = Array(n).fill(null);
  const answer = fibonacci(arr, n);

  return answer;
}

// after
function fibonacci(n) {
  let result = 0;

  if (n === 1 || n === 2) {
    return n;
  }
  let first = 1;
  let second = 1;

  for (let i = 3; i <= n; i++) {
    result = first + second;
    first = second % 1234567;
    second = result % 1234567;
  }
  return result % 1234567;
}

function solution(n) {
  return fibonacci(n);
}

// 느낀 점
// 최근에 dp를 배우고 메모이제이션을 적용했는데도, 테스트 13,14는 런타임에러가 나서 찾아보다 피사노 주기란 걸 알게됐다.
// 쉽게 풀 수 있는 문제라고 생각했는데도 100점이 안나오고 새로운 걸 배우다니,,,코테의 길은 정말 멀고도 험하다...
// 개발 잘하고 싶다...!

// 피사노 주기 - 피보나치 수를 N으로 나눈 나머지는 항상 주기를 가지게 된다는 것
