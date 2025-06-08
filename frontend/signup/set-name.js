// DOM 요소 가져오기
const nameInput = document.getElementById("name-input");
const completeBtn = document.getElementById("complete-btn");

// 입력값 변화 감지 - 빈 값 아니면 버튼 활성화
nameInput.addEventListener("input", () => {
  if (nameInput.value.trim() !== "") {
    completeBtn.disabled = false;
    completeBtn.classList.add("active");
  } else {
    completeBtn.disabled = true;
    completeBtn.classList.remove("active");
  }
});

// 완료 버튼 클릭 시 비활성화 상태 아니면 메인 페이지로 이동
completeBtn.addEventListener("click", () => {
  if (!completeBtn.disabled) {
    // 필요시 localStorage 저장 가능
    window.location.href = "../main/main.html";
  }
});


// 뒤로가기 아이콘 클릭 시 히스토리 백
document.getElementById("back-button").addEventListener("click", () => {
  history.back();
});
