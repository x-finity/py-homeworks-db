SELECT COUNT(artist_id), "name"
	FROM public.artistsgenre ag
	LEFT JOIN genres g ON ag.genre_id = g.id 
	GROUP BY "name";

SELECT COUNT(*), release_year
	FROM public.tracks t 
	JOIN albums a ON t.album_id = a.id
	WHERE release_year BETWEEN 2019 AND 2020
	GROUP BY release_year;

SELECT AVG(duration), al.title
	FROM public.tracks t 
	LEFT JOIN albums al ON t.album_id = al.id 
	GROUP BY al.title;

SELECT a.name, release_year
	FROM public.artistsalbum aa
	JOIN artists a ON aa.artist_id = a.id
	JOIN albums al ON aa.album_id = al.id
	WHERE release_year != 2020;

SELECT c.title, a.name
	FROM public.collectionstracks ct
	JOIN collections c ON ct.collection_id = c.id 
	JOIN tracks t ON ct.track_id = t.id 
	JOIN albums al ON t.album_id = al.id 
	JOIN artistsalbum aa ON aa.album_id = al.id
	JOIN artists a ON aa.artist_id = a.id
	WHERE a."name" = 'Queen';