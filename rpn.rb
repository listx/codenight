#!/usr/bin/env ruby

def evaluate(equation_str)
	terms = equation_str.split(' ').reverse
	stack = []
	while terms.size > 0
		term = terms.pop
		case term
		when '+', '-', '*'
			b = stack.pop
			a = stack.pop
			op = term.to_sym
			c = b.send(op, a)
			stack.push(c)
		when /^\d+?$/
			stack.push(term.to_i)
		else
			raise "invalid input `#{term}'"
		end
	end
	stack
end
