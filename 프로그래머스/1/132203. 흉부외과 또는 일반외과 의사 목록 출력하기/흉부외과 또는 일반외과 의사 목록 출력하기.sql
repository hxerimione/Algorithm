-- 코드를 입력하세요
SELECT dr_name,dr_id, MCDP_CD,date_format(hire_ymd,"%Y-%m-%d") as HIRE_YND
from doctor
where MCDP_CD ="GS" or MCDP_CD ="CS"
order by hire_ymd desc, dr_name asc