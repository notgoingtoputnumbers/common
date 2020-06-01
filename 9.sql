select name
from movies join (stars join people on person_id = id)
on movies.id = stars.movie_id
where year = 2004
order by birth desc