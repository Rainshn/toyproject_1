document.addEventListener('DOMContentLoaded', () => {
  // 로그인 시 → main.html로 이동
  const loginForm = document.getElementById('loginForm');
  loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    window.location.href = '../main/main.html';
  });

  // 회원가입 버튼 클릭 시 → signup.html로 이동
  const signupBtn = document.getElementById('signupBtn');
  signupBtn.addEventListener('click', () => {
    window.location.href = '../signup/signup.html';
  });

  // Google 로그인 모달 처리
  const googleBtn = document.getElementById('googleLoginBtn');
  const modal = document.getElementById('googleModal');
  const cancelBtn = document.getElementById('cancelBtn');
  const continueBtn = document.getElementById('continueBtn');

  // 구글 버튼 클릭 시 모달 표시
  googleBtn.addEventListener('click', () => {
    modal.classList.remove('hidden');
  });

  // 취소 버튼 클릭 시 모달 숨김
  cancelBtn.addEventListener('click', () => {
    modal.classList.add('hidden');
  });

  // 계속 버튼 클릭 시 구글 로그인 시도
  continueBtn.addEventListener('click', () => {
    // 실제 구글 OAuth 인증 URL로 교체 필요
    window.location.href = 'https://accounts.google.com/o/oauth2/v2/auth?...';
  });
});
