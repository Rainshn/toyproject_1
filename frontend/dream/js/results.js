document.addEventListener('DOMContentLoaded', function() {
    // 현재 페이지의 주제가 되는 꿈의 제목 (헤더 타이틀과 동일)
    const currentDreamTitle = '오징어가 나오는 꿈';

    // 1. '관련된 꿈' 찾아내기
    // MASTER_DREAM_DATA에서 현재 제목과 일치하는 꿈을 필터링함 (임시로)
    const relatedDreams = MASTER_DREAM_DATA.filter(dream => dream.title === currentDreamTitle);

    // 2. '비슷한 꿈' 찾아내기 (현재는 UI 디자인에 따라 빈 배열로 처리)
    // 추후 AI API가 비슷한 꿈을 반환하면 이 부분에 로직을 추가할 예정
    const similarDreams = [];

    // 3. 화면에 데이터 렌더링
    const relatedListContainer = document.getElementById('related-dreams-list');
    const similarListContainer = document.getElementById('similar-dreams-list');
            
    // 4. '관련된 꿈' 목록 채우기
    relatedDreams.forEach(dream => {
        const listItem = `
            <div class="dream-list-item">
                <a href="./dream-detail.html?id=${dream.id}">
                    <span>${dream.title}</span>
                    <span class="arrow">&gt;</span>
                </a>
            </div>
        `;
        relatedListContainer.innerHTML += listItem;
    });
            
    // 5. '비슷한 꿈' 목록 채우기 (조건부 렌더링)
    if (similarDreams.length === 0) {
        // 데이터가 없으면 "없음" 메시지 표시
        similarListContainer.innerHTML = `
            <div class="no-dreams-item">
                <span class="no-dreams-message">비슷한 꿈이 없어요</span>
            </div>
        `;
    } else {
        // 데이터가 있으면 목록 표시
        similarDreams.forEach(dream => {
            const listItem = `
                 <div class="dream-list-item">
                    <a href="/dream-detail?id=${dream.id}">
                        <span>${dream.title}</span>
                        <span class="arrow">&gt;</span>
                    </a>
                </div>
            `;
            similarListContainer.innerHTML += listItem;
        });
    }
});