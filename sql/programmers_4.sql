-- 자동차 대여 기록에서 장기/단기 대여 구분하기
-- 오늘 대여하고 오늘 반납해도 대여 기간은 하루
-- DATE Type

SELECT  HISTORY_ID 
        , CAR_ID
        , DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE
        , DATE_FORMAT(END_DATE, '%Y-%m-%d') AS END_DATE
        , CASE
        WHEN DATEDIFF(END_DATE,START_DATE) + 1 >= 30 THEN "장기 대여"
        ELSE "단기 대여"
        END AS RENT_TYPE
FROM  CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE  START_DATE BETWEEN '2022-09-01' AND '2022-09-30'
ORDER BY  HISTORY_ID DESC;
