-- lists all genre and displays the number of shows linked to each
-- Each records should display <TV Show genre>
-- - <Number of shows linked to this genre>
-- first column must be called genre
-- second column must be called number_of_shows
-- Don't display a genre that doesn't have any shows linked
-- must be sorted in descending order by the number of shows linked

SELECT tv_genres.name AS genre, COUNT(DISTINCT tv_show_genres.show_id)
AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
	ON tv_shows.id = tv_show_genres.show_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
