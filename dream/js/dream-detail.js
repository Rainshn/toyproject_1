let currentDream = null;

document.addEventListener('DOMContentLoaded', function() {
    const urlParams = new URLSearchParams(window.location.search);
    const dreamId = urlParams.get('id');
    currentDream = MASTER_DREAM_DATA.find(d => d.id === dreamId);

    if (currentDream) {
        document.getElementById('dream-date').textContent = currentDream.date;
        document.getElementById('dream-title').textContent = currentDream.title;
        const interpretationContainer = document.getElementById('dream-interpretation');
        interpretationContainer.innerHTML = ''; // 기존 내용을 비워줍니다.
        currentDream.interpretation.forEach(paragraph => {
            const p = document.createElement('p');
            p.textContent = paragraph;
            interpretationContainer.appendChild(p);
        });
    } else {
        document.querySelector('main').innerHTML = '<h1>해당하는 꿈 정보를 찾을 수 없습니다.</h1>';
    }
});

/* 해몽 저장하기 로직 */
function saveDreamAndRedirect() {
    if (!currentDream) {
        alert('저장할 꿈 정보가 없습니다.');
        return;
    }
    const savedDreams = JSON.parse(localStorage.getItem('myDreamDiary') || '[]');
    const isAlreadySaved = savedDreams.some(dream => dream.id === currentDream.id);

    if (isAlreadySaved) {
        alert('이미 저장된 해몽입니다.');
    } else {
        savedDreams.push(currentDream);
        localStorage.setItem('myDreamDiary', JSON.stringify(savedDreams));
        alert('해몽이 저장되었습니다!');
    }
    // 저장 후 '꿈 기록 목록' 페이지로 이동
    window.location.href = 'saved-list.html';
}