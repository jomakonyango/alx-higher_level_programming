-- This script lists all shows and their linked genres from the database hbtn_0d_tvshows.
-- If a show doesn't have a genre, it displays NULL in the genre column.
-- Each record displays: tv_shows.title - tv_genres.name
-- Results are sorted in ascending order by the show title and genre name.

SELECT tv_shows.title, IFNULL(tv_genres.name, 'NULL') AS name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
LEFT JOIN tv_genres ON tv_show_genres.tv_genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, name ASC;
