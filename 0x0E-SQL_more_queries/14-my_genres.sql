-- Script that uses the hbtn_0d_tvshows database to lists all genres of Dexter.
-- The tv_shows table contains only one record where title = Dexter (id c/b dif)
SELECT g.`name`
FROM `tv_genres` AS g
     INNER JOIN `tv_show_genres` AS sg
          ON g.`id` = sg.`genre_id`
     INNER JOIN `tv_shows` AS s
          ON sg.`show_id` = s.`id`
WHERE s.`title` = 'Dexter'
ORDER BY g.`name` ASC;
