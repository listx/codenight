import Data.Char (isDigit)

data Term
	= TermInt Integer
	| TermOp (Integer -> Integer -> Integer)

evaluate :: String -> [Integer]
evaluate = reduce . map mkTerm . words

mkTerm :: String -> Term
mkTerm termStr = case termStr of
	"+" -> TermOp (+)
	"-" -> TermOp (-)
	"*" -> TermOp (*)
	_
		| and $ map isDigit termStr -> TermInt $ read termStr
		| otherwise -> error $ "invalid input `" ++ termStr ++ "'"

reduce :: [Term] -> [Integer]
reduce = foldl stackManip []
	where
	stackManip stack term = case term of
		TermInt n -> n : stack
		TermOp op
			| length stack < 2
				-> error "stack too small for operator application"
			| otherwise -> let
				a = stack!!0
				b = stack!!1
				c = op a b
				in c : drop 2 stack
