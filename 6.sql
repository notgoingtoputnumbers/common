select avg(rating)
from movies join ratings
on id = movie_id
where year = 2012