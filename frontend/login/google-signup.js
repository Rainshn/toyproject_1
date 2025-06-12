document.addEventListener('DOMContentLoaded', () => {
  // URL에서 email 파라미터 추출
  const urlParams = new URLSearchParams(window.location.search);
  const email = urlParams.get('email');

  // 요소 선택
  const emailInput = document.getElementById('email');
  const allAgree = document.getElementById('allAgree');
  const requiredChecks = document.querySelectorAll('.required');
  const allChecks = document.querySelectorAll('input[type="checkbox"]:not(#allAgree)');
  const submitBtn = document.getElementById('submitBtn');

  // 이메일 입력값 설정
  if (email) {
    emailInput.value = email;
  }

  // 가입 버튼 활성화 여부 업데이트 함수
  function updateSubmitButtonState() {
    const allRequiredChecked = [...requiredChecks].every(cb => cb.checked);
    submitBtn.disabled = !allRequiredChecked;
    submitBtn.style.backgroundColor = allRequiredChecked ? '#2F80ED' : 'gray';
  }

  // 전체 동의 체크 시 모든 항목 체크/해제
  allAgree.addEventListener('change', () => {
    allChecks.forEach(cb => cb.checked = allAgree.checked);
    updateSubmitButtonState();
  });

  // 개별 체크박스 변경 시 전체 동의 상태 갱신 및 버튼 상태 갱신
  allChecks.forEach(cb => {
    cb.addEventListener('change', () => {
      const isAllChecked = [...allChecks].every(cb => cb.checked);
      allAgree.checked = isAllChecked;
      updateSubmitButtonState();
    });
  });

  // 가입하기 버튼 클릭 시 페이지 이동
  submitBtn.addEventListener('click', () => {
    if (!submitBtn.disabled) {
      // 모든 필수 체크박스가 선택된 경우에만 진행
      window.location.href = '../signup/complete.html';
    }
  });

  // 페이지 로드시 버튼 초기 상태 반영
  updateSubmitButtonState();
});
