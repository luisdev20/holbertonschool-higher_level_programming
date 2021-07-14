-- Script that lists all genres from hbtn_0d_tvshows and displays the number of
-- shows linked to each.
SELECT g.`name` AS 'genre', COUNT(g.`name`) AS 'number_of_shows'
FROM tv_show_genres AS sg INNER JOIN tv_genres AS g
    ON g.`id` = sg.`genre_id`
GROUP BY `genre`
ORDER BY `number_of_shows` DESC;
