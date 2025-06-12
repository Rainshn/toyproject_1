document.addEventListener('DOMContentLoaded', function() {
    const listContainer = document.getElementById('dream-list-container');

    // 로컬 스토리지에서 데이터 불러오기
    let savedDreams = JSON.parse(localStorage.getItem('myDreamDiary') || '[]');

    // 데이터가 없으면 mock-data.js의 샘플 데이터로 초기화
    if (savedDreams.length === 0) {
        savedDreams = MASTER_DREAM_DATA.slice(0, 5); // 5개 샘플 데이터 사용
        localStorage.setItem('myDreamDiary', JSON.stringify(savedDreams));
        
        const initialMessage = document.createElement('div');
        initialMessage.className = 'no-dreams';
        initialMessage.innerHTML = '샘플 꿈 기록을 저장했어요.<br>꿈 해몽을 저장하고 나만의 기록장을 채워보세요.';
        listContainer.appendChild(initialMessage);
    }
    
    renderDreamList(savedDreams);

    function renderDreamList(dreams) {
        listContainer.innerHTML = ''; // 목록을 새로 그리기 전에 비워줍니다.

        // 날짜 기준 최신순으로 정렬
        dreams.sort((a, b) => new Date(b.date.replace(/\./g, '-')) - new Date(a.date.replace(/\./g, '-')));

        dreams.forEach(dream => {
            // 각 꿈 항목을 클릭하면 dream_detail.html로 id와 함께 이동하는 링크
            const dreamItemHTML = `
                <a href="records.html?id=${dream.id}" class="dream-card">
                    <div class="card-title">${dream.title}</div>
                    <div class="card-snippet">${dream.snippet}</div>
                    <div class="card-date">${dream.date}</div>
                </a>
            `;
            listContainer.innerHTML += dreamItemHTML;
        });
    }
});