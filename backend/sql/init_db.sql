-- MySql로 데이터베이스를 조회하기 위해 생성한 파일입니다.
-- backend 경로에 위치한 '.env.example' 텍스트 파일을 참고하셔서,
-- 자신의 컴퓨터 환경에 맞는 내용을 입력해 주시면 됩니다.

CREATE DATABASE toyproject;

USE toyproject;
SHOW tables;

-- 회원가입한 유저 목록 조회
SELECT id, username, email, nickname FROM accounts_customuser;

-- 작성한 글 목록 조회
SELECT d.id, d.title, d.context, d.tags, d.feelings, u.id AS user_id, u.username
FROM dreams_dreamrecord d
JOIN accounts_customuser u ON d.user_id = u.id
ORDER BY d.id ASC;

-- 모든 회원 삭제 (주의!)
SET SQL_SAFE_UPDATES = 0;
SET FOREIGN_KEY_CHECKS = 0;
DELETE FROM accounts_customuser;
SET SQL_SAFE_UPDATES = 1;
SET FOREIGN_KEY_CHECKS = 1;

-- 특정 username을 가진 사용자 삭제
SET SQL_SAFE_UPDATES = 0;
SET FOREIGN_KEY_CHECKS = 0;
DELETE FROM accounts_customuser WHERE username = 'rainshn1';
SET SQL_SAFE_UPDATES = 1;
SET FOREIGN_KEY_CHECKS = 1;
