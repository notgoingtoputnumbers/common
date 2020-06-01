select count(title)
from movies join ratings
on id = movie_id
where rating = 10