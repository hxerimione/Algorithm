select count(user_id) as users
from user_info
where joined like '2021%' 
and age >=20 and age<=29