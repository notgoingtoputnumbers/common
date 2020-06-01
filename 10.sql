select name
from people join (directors join ratings on directors.movie_id = ratings.movie_id)
on id = person_id
where rating >= 9