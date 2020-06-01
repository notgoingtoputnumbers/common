select  movies.title, rating, year
from movies join (stars join people on person_id = id)
on movies.id = stars.movie_id 
join ratings on movies.id = ratings.movie_id
where name = "Aleksandr Domogarov" and birth = 1963
order by rating desc
limit 99