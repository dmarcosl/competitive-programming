select case when g.grade > 7 then s.name else NULL end, g.grade, s.marks
from students s
inner join grades g on s.marks between g.min_mark and g.max_mark
order by 2 desc, 1, 3 asc;