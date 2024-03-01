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

