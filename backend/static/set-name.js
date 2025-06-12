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
completeBtn.addEventListener("click", async () => {
 if (!completeBtn.disabled) {
    const nickname = nameInput.value.trim();
    try {
      const response = await fetch("http://127.0.0.1:8000/accounts/nickname/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        credentials: "include", // 세션/쿠키 인증 시 필요
        body: JSON.stringify({ nickname }),
      });
      if (response.ok) {
        // 성공 시 메인 페이지 이동
        window.location.href = "http://127.0.0.1:8000/";
      } else {
        const data = await response.json();
        alert(data.error || "닉네임 설정에 실패했습니다.");
      }
    } catch (e) {
      alert("서버와 통신에 실패했습니다.");
    }
  }
});


// 뒤로가기 아이콘 클릭 시 히스토리 백
document.getElementById("back-button").addEventListener("click", () => {
  history.back();
});
