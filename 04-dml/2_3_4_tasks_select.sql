/* 2 task */
SELECT title, duration 
	FROM public.tracks
	WHERE duration = (SELECT max(duration) FROM public.tracks);

SELECT title
	FROM public.tracks
	WHERE duration >= 230;

SELECT title
	FROM public.collections
	WHERE release_year BETWEEN 2018 AND 2020;

SELECT "name"
	FROM public.artists
	WHERE "name" NOT LIKE '% %';

SELECT title 
	FROM public.tracks
	WHERE (title LIKE '%my%' OR title LIKE '%мой%');

/* 3 task */
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

/* 4 task */
SELECT al.title
	FROM public.albums al
	JOIN artistsalbum aa ON al.id = aa.album_id 
	JOIN artists a ON aa.artist_id = a.id 
	JOIN artistsgenre ag ON a.id = ag.artist_id 
	JOIN genres g ON ag.genre_id = g.id 
	GROUP BY al.title
	HAVING COUNT(g.name) > 1
	ORDER BY al.title;

SELECT t.title
	FROM public.tracks t
	LEFT JOIN collectionstracks ct ON t.id = ct.track_id 
	WHERE ct.track_id IS null;

SELECT a.name
	FROM public.artists a
	JOIN artistsalbum aa ON a.id = aa.artist_id 
	JOIN albums al ON aa.album_id = al.id 
	JOIN tracks t ON al.id = t.album_id 
	WHERE t.duration = (SELECT MIN(duration) FROM tracks);

SELECT al.title, COUNT(*)
	FROM public.albums al
	JOIN tracks t ON al.id = t.album_id
	GROUP BY al.title
	HAVING COUNT(*) = (SELECT COUNT(*)
		FROM public.albums al
		JOIN tracks t ON al.id = t.album_id
		GROUP BY al.title
		ORDER BY COUNT(*) LIMIT 1);