-- Uses the hbtn_0d_tvshows db to lists all genrees of the show Dexter
-- tv_shows table contains only one record where title = Dexter
-- but id can be different
-- results must be sorted in ascending order by the genre name

SELECT g.name AS genre
FROM tv_genres g
INNER JOIN tv_show_genres tsg ON g.id = tsg.genre_id
INNER JOIN tv_shows ts ON ts.id = tsg.show_id
WHERE ts.title = "Dexter"
ORDER BY g.name ASC;
