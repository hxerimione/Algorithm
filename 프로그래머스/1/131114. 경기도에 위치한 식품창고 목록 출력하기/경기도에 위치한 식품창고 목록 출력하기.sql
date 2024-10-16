select WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, IFNULL(FREEZER_YN,"N") AS FREEZER_YN
from food_warehouse
where address like "경기도%"
order by WAREHOUSE_ID