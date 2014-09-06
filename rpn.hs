import Data.Char (isDigit)

data Term
	= TermInt Int
	| TermOp (Int -> Int -> Int)

evaluate :: String -> [Int]
evaluate = reduce . mkTerms

mkTerms :: String -> [Term]
mkTerms = map mkTerm . words

mkTerm :: String -> Term
mkTerm termStr = case termStr of
	"+" -> TermOp (+)
	"-" -> TermOp (-)
	"*" -> TermOp (*)
	_
		| all (==True) $ map isDigit termStr -> let
			n = read termStr :: Int
			in TermInt n
		| otherwise -> error $ "invalid input `" ++ termStr ++ "'"

reduce :: [Term] -> [Int]
reduce = foldl f []
	where
	f stack term = case term of
		TermInt n -> n : stack
		TermOp op
			| length stack < 2
				-> error "stack too small for operator application"
			| otherwise -> let
				a = stack!!0
				b = stack!!1
				in op a b : drop 2 stack
