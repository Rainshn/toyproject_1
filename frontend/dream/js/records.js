document.addEventListener('DOMContentLoaded', function() {
    // DOM 요소 가져오기
    const headerEl = document.getElementById('detail-header');
    const contentEl = document.getElementById('dream-detail-content');
    const optionsMenuEl = document.getElementById('options-menu');
    const editButton = document.getElementById('edit-button');
    const deleteButton = document.getElementById('delete-button');

    // URL에서 꿈 ID 가져오기
    const urlParams = new URLSearchParams(window.location.search);
    const dreamId = urlParams.get('id');

    // 로컬 스토리지에서 모든 꿈 데이터 가져오기
    let allDreams = JSON.parse(localStorage.getItem('myDreamDiary') || '[]');
    // 현재 페이지의 꿈 데이터 찾기
    let currentDream = allDreams.find(dream => dream.id === dreamId);

    // 1. 보기 모드 렌더링 함수
    function renderViewMode() {
        // 헤더 렌더링
        headerEl.innerHTML = `
            <a href="saved-list.html" class="back-arrow">&lt;</a>
            <span>${currentDream.date}</span>
            <span id="more-options-button" class="more-options"><img src="../images/span-add.png" alt="더보기"></span>
        `;

        // 콘텐츠 렌더링
        const interpretationHTML = currentDream.interpretation.map(p => `<p>${p}</p>`).join('');
        const userDreamText = `${currentDream.title}을 꿨어요!\n${currentDream.snippet}\n꿈이었는데 어떤 의미가 있는걸까요?`;
        contentEl.innerHTML = `
            <div class="user-dream-box">
                <h2>${currentDream.title}</h2>
                <p>${userDreamText}</p>
                <div class="tags">
                    <span>#나</span><span>#오징어</span> 
                    <span class="emoji">😃</span>
                </div>
            </div>
            <section class="interpretation-section">
                <h3>저장한 해몽</h3>
                <div class="interpretation-content">${interpretationHTML}</div>
            </section>
        `;

        // '...' 버튼에 이벤트 리스너 추가
        document.getElementById('more-options-button').addEventListener('click', (e) => {
            e.stopPropagation(); // 이벤트 버블링 방지
            optionsMenuEl.classList.toggle('active');
        });
    }

    // 4. 꿈 기록 삭제 함수
    function deleteDream() {
        const isConfirmed = window.confirm('이 기록을 삭제합니다.');
        if (isConfirmed) {
            // 현재 꿈을 제외한 나머지 꿈들만 필터링
            const remainingDreams = allDreams.filter(dream => dream.id !== dreamId);
            localStorage.setItem('myDreamDiary', JSON.stringify(remainingDreams));
            // 목록 페이지로 이동
            window.location.href = 'saved-list.html';
        }
    }

    // 초기 실행 로직
    if (currentDream) {
        // 처음엔 보기 모드로 시작
        renderViewMode();

        // 수정/삭제 버튼 이벤트 리스너
        editButton.addEventListener('click', () => {
            optionsMenuEl.classList.remove('active');
            renderEditMode();
            //window.location.href = `../record/record.html?editId=${dreamId}`;

        });

        deleteButton.addEventListener('click', deleteDream);

        // 메뉴 바깥을 클릭하면 메뉴 닫기
        document.body.addEventListener('click', () => {
            if (optionsMenuEl.classList.contains('active')) {
                optionsMenuEl.classList.remove('active');
            }
        });
    } else {
        headerEl.innerHTML = `<a href="index.html" class="back-arrow">&lt;</a>`;
        contentEl.innerHTML = `<p class="no-dreams">해당 꿈 기록을 찾을 수 없습니다.</p>`;
    }
});