-- 코드를 입력하세요
SELECT round(AVG(daily_fee)) as average_fee

from CAR_RENTAL_COMPANY_CAR
where car_type = 'SUV'