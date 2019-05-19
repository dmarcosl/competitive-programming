select name
from students
where marks > 75
order by reverse(substring(reverse(name), 1, 3)), id;