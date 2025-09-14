-- 조건에 부합하는 중고거래 댓글 조회하기
-- DATE_FORMAT
-- %Y Year - Year (4-digit format)
-- %y Year - Last 2 digits of the year
-- %M Month - Month name (January ~ December)
-- %m Month - Month number (00 ~ 12)
-- %d Day (00 ~ 31)

-- JOIN ON

-- SUBSTR
-- Extract a substring from a string

SELECT A.TITLE
       , B.BOARD_ID
       , B.REPLY_ID
       , B.WRITER_ID
       , B.CONTENTS
       , DATE_FORMAT(B.CREATED_DATE, '%Y-%m-%d') AS CRAETED_DATE
FROM USED_GOODS_BOARD AS A
INNER
JOIN USED_GOODS_REPLY AS B
ON A.BOARD_ID = B.BOARD_ID
WHERE SUBSTR(A.CREATED_DATE,1,7) = '2022-10'
ORDER BY B.CREATED_DATE ASC, A.TITLE ASC;
