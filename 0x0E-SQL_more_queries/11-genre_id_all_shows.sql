-- Script that lists all shows contained in the database hbtn_0d_tvshows.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id.
SELECT s.`title`, sg.`genre_id`
    FROM tv_shows AS s
        LEFT OUTER JOIN tv_show_genres AS sg
        ON s.`id` = sg.`show_id`
    ORDER BY s.`title` ASC, sg.`genre_id` ASC;
