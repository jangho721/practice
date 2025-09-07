-- 특정 형질을 가지는 대장균 찾기
-- Output the result in the COUNT column
-- Bitwise operator

SELECT COUNT(*) AS COUNT 
FROM ECOLI_DATA
WHERE 1=1
    AND GENOTYPE & 2 = 0
    AND (GENOTYPE & 4 = 4 OR GENOTYPE & 1 = 1);
