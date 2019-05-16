select s.id, s.age, s.coins_needed, s.power
from (
    select w.id, wp.age, w.coins_needed, w.power
    from Wands as w
    inner join Wands_Property as wp on w.code = wp.code
) as s
inner join (
    select wp.age, min(w.coins_needed) as coins_needed, w.power
    from Wands as w
    inner join Wands_Property as wp on w.code = wp.code
    where wp.is_evil = 0
    group by wp.age, w.power
    order by w.power desc, wp.age desc
) as t on s.age = t.age and s.coins_needed = t.coins_needed and s.power = t.power
order by t.power desc, t.age desc;