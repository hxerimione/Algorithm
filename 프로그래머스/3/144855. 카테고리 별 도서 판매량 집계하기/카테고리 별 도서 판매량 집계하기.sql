select a.category, sum(b.sales)
from book as a 
join (select book_id,sum(sales) as sales
     from book_sales
     where sales_date like "2022-01%"
     group by book_id) as b on a.book_id = b.book_id

group by a.category
order by a.category
