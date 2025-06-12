const userId = document.getElementById("user-id");
const checkIdBtn = document.getElementById("check-id");
const password = document.getElementById("password");
const confirmPassword = document.getElementById("confirm-password");
const checkAll = document.getElementById("check-all");
const requiredChecks = document.querySelectorAll(".terms.required");
const allChecks = document.querySelectorAll(".terms");
const submitBtn = document.getElementById("submit-btn");

// 에러 메시지 요소
const pwLengthError = document.getElementById("pw-length-error");
const pwMatchError = document.getElementById("pw-match-error");

// 아이디 중복확인 상태 변수
let isIdChecked = false;

// 아이디 중복확인 버튼 클릭 시 처리
checkIdBtn.addEventListener("click", () => {
  if (userId.value.trim() !== "") {
    isIdChecked = true;                     // 중복확인 완료 상태로 변경
    checkIdBtn.classList.add("active");    // 버튼 활성화 스타일 적용
    validateForm();                        // 폼 유효성 재검사
  }
});

// 전체 동의 체크박스 변경 시 모든 약관 체크박스 상태 동기화
checkAll.addEventListener("change", (e) => {
  allChecks.forEach(cb => cb.checked = e.target.checked);
  validateForm();
});

// 개별 약관 체크박스 변경 시 폼 유효성 검사
allChecks.forEach(cb => {
  cb.addEventListener("change", validateForm);
});

// 아이디, 비밀번호, 비밀번호 확인 입력 시 폼 유효성 검사
[userId, password, confirmPassword].forEach(el =>
  el.addEventListener("input", validateForm)
);

// 폼 유효성 검사 함수
function validateForm() {
  const pwVal = password.value;
  const confirmVal = confirmPassword.value;

  // 비밀번호 길이 유효성 (8~16자)
  const isLengthValid = pwVal.length >= 8 && pwVal.length <= 16;

  // 비밀번호와 비밀번호 확인 일치 여부
  const isMatch = pwVal === confirmVal && pwVal !== "";

  // 비밀번호 길이 오류 표시 토글
  pwLengthError.style.display = (!isLengthValid && pwVal) ? "block" : "none";

  // 비밀번호 일치 오류 표시 토글
  pwMatchError.style.display = (!isMatch && confirmVal) ? "block" : "none";

  // 필수 약관 모두 체크 여부
  const allRequiredChecked = Array.from(requiredChecks).every(cb => cb.checked);

  // 제출 버튼 활성화 조건
  if (
    userId.value.trim() &&       // 아이디 입력됨
    isIdChecked &&               // 아이디 중복확인 완료
    isLengthValid &&             // 비밀번호 길이 유효
    isMatch &&                   // 비밀번호 일치
    allRequiredChecked           // 필수 약관 동의 완료
  ) {
    submitBtn.disabled = false;
    submitBtn.classList.add("active");
  } else {
    submitBtn.disabled = true;
    submitBtn.classList.remove("active");
  }
}

// 이전으로 가기 버튼 클릭 이벤트
document.getElementById("back-button").addEventListener("click", () => {
  history.back();
});

// 제출 버튼 클릭 이벤트 처리
submitBtn.addEventListener("click", (e) => {
  e.preventDefault(); // 기본 제출 방지

  // 버튼이 활성화된 경우에만 이동 처리
  if (!submitBtn.disabled) {
    window.location.href = "../signup/complete.html";
  }
});
