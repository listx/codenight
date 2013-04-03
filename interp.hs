{-# Language RecordWildCards #-}

import Data.List
import Data.Maybe

probStr :: String
probStr = "--------------++++++++++-++++----++++++++----x---------------++++-+-+---+++++"

data Com
	= Minus
	| Plus
	| Swap
	| KeepSwapping
	deriving (Enum, Ord, Eq, Show)

commandLegend :: [(Char, Com)]
commandLegend = zip (map showChar' cs) $ cs
	where
	cs = enumFrom Minus

showChar' :: Com -> Char
showChar' com = case com of
	Minus -> '-'
	Plus -> '+'
	Swap -> 'x'
	KeepSwapping -> 'X'

numCom :: Com -> Interp -> (Int -> Int)
numCom com Interp{..} = case com of
	Plus -> if swapPM then sub1 else add1
	Minus -> if swapPM then add1 else sub1
	_ -> error $ "non-numeric operator " ++ show com ++ " detected"

add1, sub1 :: Int -> Int
add1 = (+1)
sub1 = (+(-1))

data Interp = Interp
	{ numVal :: Int
	, swapPM :: Bool
	, keepSwapping :: Bool
	}

solve :: String -> Int
solve = numVal . foldl' step Interp
	{ numVal = 0
	, swapPM = False
	, keepSwapping = False
	}
	where
	step interp@Interp{..} c = case lookup c commandLegend of
		Just com
			| com == Swap -> interp {swapPM = not swapPM}
			| com == KeepSwapping -> interp {keepSwapping = not keepSwapping}
			| otherwise -> if keepSwapping
				then interp
					{ numVal = numCom com interp {swapPM = not swapPM} numVal
					, swapPM = not swapPM
					}
				else interp {numVal = numCom com interp numVal}
		Nothing -> error $ "invalid character `" ++ show c ++ "' detected"
