-- This script lists all genres from hbtn_0d_tvshows_rate by their rating.
-- Each record displays: tv_genres.name - rating sum
-- Results are sorted in descending order by their rating.

SELECT tv_genres.name, SUM(rating) AS rating
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.tv_genre_id
JOIN tv_show_ratings ON tv_show_genres.tv_show_id = tv_show_ratings.tv_show_id
GROUP BY tv_genres.name
ORDER BY rating DESC;
