module Map where

data Tile
	= Plains
	| Forest
	| Portal
	| Castle
	deriving (Show)

type Coord = (Int, Int) -- (x, y)

data Room = Room
	{ roomDesc :: String
	, roomMP :: Int
	}

data GameMap = GameMap
	{ gmAscii :: String
	, gmTiles :: [(Coord, Room)]
	}

legend :: [(Char, Tile)]
legend =
	[ ('.', Plains)
	, ('#', Forest)
	, ('P', Portal)
	, ('C', Castle)
	]

defaultMapStr :: String
defaultMapStr = "\
\#.........\n\
\#.........\n\
\#....P....\n\
\#.....C...\n\
\#........."

importMap :: [String] -> GameMap
importMap strs = map getRooms strs
	where
	getRooms :: String -> [(Coord, Room)]
	getRooms str = map getRoom str
	getRoom :: Char -> (Coord, Room)
	getRoom c = case lookup c legend of
		Just t -> show t
		Nothing -> error $ "character" ++ squote c ++ "not found in legend"

squote :: String -> String
squote s = " `" ++ s ++ "' "
