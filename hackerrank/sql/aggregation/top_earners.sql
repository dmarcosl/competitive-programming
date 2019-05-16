select max(salary * months), count(*)
from employee
group by salary * months
order by 1 desc
limit 1;