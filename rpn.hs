import Data.Char (isDigit)

data Term
	= TermInt Int
	| TermOp (Int -> Int -> Int)

evaluate :: String -> [Int]
evaluate equationStr = reduce terms
	where
	terms = mkTerms equationStr

mkTerms :: String -> [Term]
mkTerms equationStr = map mkTerm termsStrAry
	where
	termsStrAry = words equationStr

mkTerm :: String -> Term
mkTerm termStr = case termStr of
	"+" -> TermOp (+)
	"-" -> TermOp (-)
	"*" -> TermOp (*)
	_
		| allDigits termStr -> let
			n = read termStr :: Int
			in TermInt n
		| otherwise -> error $ "invalid input `" ++ termStr ++ "'"

reduce :: [Term] -> [Int]
reduce ts = foldl f [] ts
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

allDigits :: String -> Bool
allDigits = all (==True) . map isDigit
