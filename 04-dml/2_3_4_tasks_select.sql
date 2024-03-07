/* 2 task */
-- 2.1
SELECT title, duration 
	FROM public.tracks
	WHERE duration = (SELECT max(duration) FROM public.tracks);

-- 2.2
SELECT title
	FROM public.tracks
	WHERE duration >= 210;

-- 2.3
SELECT title
	FROM public.collections
	WHERE release_year BETWEEN 2018 AND 2020;

-- 2.4
SELECT "name"
	FROM public.artists
	WHERE "name" NOT LIKE '% %';

-- 2.5
SELECT title 
	FROM public.tracks
	WHERE string_to_array(lower(title), ' ') && ARRAY['my', 'мой'];

/* 3 task */
-- 3.1
SELECT COUNT(artist_id), "name"
	FROM public.artistsgenre ag
	LEFT JOIN genres g ON ag.genre_id = g.id 
	GROUP BY "name";

-- 3.2
SELECT COUNT(*)
	FROM public.tracks t 
	JOIN albums al ON t.album_id = al.id
	WHERE al.release_year BETWEEN 2019 AND 2020;

-- 3.3
SELECT AVG(duration), al.title
	FROM public.tracks t 
	LEFT JOIN albums al ON t.album_id = al.id 
	GROUP BY al.title;

-- 3.4
SELECT a.name
	FROM public.artists a
	WHERE a.name NOT IN (
		SELECT a.name
		FROM public.artistsalbum aa
		JOIN artists a ON aa.artist_id = a.id
		JOIN albums al ON aa.album_id = al.id
		WHERE release_year = 2020);

-- 3.5
SELECT c.title, a.name
	FROM public.collectionstracks ct
	JOIN collections c ON ct.collection_id = c.id 
	JOIN tracks t ON ct.track_id = t.id 
	JOIN albums al ON t.album_id = al.id 
	JOIN artistsalbum aa ON aa.album_id = al.id
	JOIN artists a ON aa.artist_id = a.id
	WHERE a."name" = 'Queen';

/* 4 task */
-- 4.1
SELECT DISTINCT al.title
	FROM public.albums al
	JOIN artistsalbum aa ON al.id = aa.album_id 
	JOIN artists a ON aa.artist_id = a.id 
	JOIN artistsgenre ag ON a.id = ag.artist_id  
	GROUP BY al.title, ag.artist_id
	HAVING COUNT(ag.genre_id) > 1
	ORDER BY al.title;

-- 4.2
SELECT t.title
	FROM public.tracks t
	LEFT JOIN collectionstracks ct ON t.id = ct.track_id 
	WHERE ct.track_id IS null;

-- 4.3
SELECT a.name
	FROM public.artists a
	JOIN artistsalbum aa ON a.id = aa.artist_id 
	JOIN albums al ON aa.album_id = al.id 
	JOIN tracks t ON al.id = t.album_id 
	WHERE t.duration = (SELECT MIN(duration) FROM tracks);

-- 4.4
SELECT al.title, COUNT(*)
	FROM public.albums al
	JOIN tracks t ON al.id = t.album_id
	GROUP BY al.title
	HAVING COUNT(*) = (SELECT COUNT(*)
		FROM public.albums al
		JOIN tracks t ON al.id = t.album_id
		GROUP BY al.title
		ORDER BY COUNT(*) LIMIT 1);