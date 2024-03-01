INSERT INTO public.genres (name) VALUES
	 ('rock'),
	 ('pop'),
	 ('rap');

INSERT INTO public.artists (name) VALUES
	('Led Zeppelin'),
	('Queen'),
	('Lady Gaga'),
	('Taylor Swift'),
	('Eminem'),
	('Nas');
	
INSERT INTO public.albums (title , release_year) VALUES
	('Led Zeppelin', 1969),
	('Queen', 1973),
	('Artpop', 2013),
	('Reputation', 2017),
	('The Eminem Show', 2002),
	('Illmatic', 1994),
	('Mix album', 2020);

INSERT INTO public.artistsgenre VALUES
	(1,1),
	(2,1),
	(3,2),
	(4,2),
	(5,3),
	(6,3);

INSERT INTO public.artistsalbum VALUES
	(1,1),
	(2,2),
	(3,3),
	(4,4),
	(5,5),
	(6,6),
	(2,7),
	(5,7),
	(3,7);

INSERT INTO public.tracks (duration, title, album_id) VALUES
	(166,'Good Times Bad Times',1),
	(388,'You Shook Me',1),
	(227,'Keep Yourself Alive',2),
	(343,'Great King Rat',2),
	(236,'Aura',3),
	(214,'Sexxx Dreams',3),
	(208,'…Ready for It?',4),
	(236,'Don’t Blame Me',4),
	(252,'Business',5),
	(290,'Without Me',5),
	(105,'The Genesis',6),
	(291,'The World Is Yours',6),
	(322,'Demo my track',6),
	(240,'Queen demo track',7),
	(150,'Eminem demo track',7),
	(301,'Lady Gaga demo track',7);

INSERT INTO public.collections (title, release_year) VALUES
	('Rock collection', 2020),
	('Pop collection', 2021),
	('Rap collection', 2022),
	('Mix Collection', 2023);

INSERT INTO public.collectionstracks VALUES
	(1,1),
	(1,3),
	(2,5),
	(2,7),
	(3,9),
	(3,11),
	(4,2),
	(4,12),
	(4,6);
