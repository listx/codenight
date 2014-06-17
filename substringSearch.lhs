\begin{code}
module Main where

import Data.List

numberOfChars :: Char -> String -> Int
numberOfChars char = foldl' step 0
	where
	step numL x
		| x == char = numL + 1
		| otherwise = numL

main :: IO ()
main = do
	putStr "enter string: "
	str <- getLine
	if null str
		then putStrLn "you're a moron"
		else do
			let
				needle = last str
				haystack = init str
				needles = numberOfChars needle haystack
			if needles == 0
				then putStrLn $ "there is no " ++ show needle ++ " in string " ++ show haystack
				else putStrLn $ "i found " ++ show needles ++ " " ++ show needle ++ " in string " ++ show haystack
\end{code}
