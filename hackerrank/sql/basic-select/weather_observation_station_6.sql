select city
from station
where lower(city) like 'a%'
or lower(city) like 'e%'
or lower(city) like 'i%'
or lower(city) like 'o%'
or lower(city) like 'u%';