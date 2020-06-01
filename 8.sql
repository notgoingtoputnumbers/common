select people.name
from movies join (stars join people
on stars.person_id = people.id)
on movies.id = stars.movie_id
where title = "Toy Story"