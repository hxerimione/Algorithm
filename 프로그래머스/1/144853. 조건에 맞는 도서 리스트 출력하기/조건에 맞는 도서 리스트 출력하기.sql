-- 코드를 입력하세요
SELECT BOOK_ID,date_format(PUBLISHED_DATE,"%Y-%m-%d") as PUBLISHED_DATE
from book
where CATEGORY='인문' and PUBLISHED_DATE <'2022-01-01' and PUBLISHED_DATE > '2020-12-31'