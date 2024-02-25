CREATE TABLE IF NOT EXISTS artists(
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS genres(
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS albums(
	id SERIAL PRIMARY KEY,
	title VARCHAR(60) NOT NULL,
	release_year SMALLINT NOT NULL
);

CREATE TABLE IF NOT EXISTS collections(
	id SERIAL PRIMARY KEY,
	title VARCHAR(60) NOT NULL,
	release_year SMALLINT NOT NULL
);


CREATE TABLE IF NOT EXISTS tracks(
	id SERIAL PRIMARY KEY,
	title VARCHAR(60) NOT NULL,
	duration SMALLINT NOT NULL CHECK(duration > 0),
	album_id INTEGER REFERENCES public.albums(id)
);

CREATE TABLE IF NOT EXISTS CollectionsTracks(
	collection_id INTEGER REFERENCES public.collections(id),
	track_id INTEGER REFERENCES public.tracks(id),
	CONSTRAINT pk PRIMARY KEY (collection_id, track_id)
);

CREATE TABLE IF NOT EXISTS ArtistsAlbum(
	artist_id INTEGER REFERENCES public.artists(id),
	album_id INTEGER REFERENCES public.albums(id),
	CONSTRAINT pk1 PRIMARY KEY (artist_id, album_id)
);

CREATE TABLE IF NOT EXISTS ArtistsGenre(
	artist_id INTEGER REFERENCES public.artists(id),
	genre_id INTEGER REFERENCES public.genres(id),
	CONSTRAINT pk2 PRIMARY KEY (artist_id, genre_id)
);
