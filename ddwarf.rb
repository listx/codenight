#2d map, "a,s,d,f" to move, "x" to exit

a = ". . . . ."
b = " . . . . "
c = "~ ~ ~ ~ ~"

aArray = [a,a,a]
pSymbol = "@"
location = [0,0]

def showMap (mapArray, coord, player)
	for i in 0..(mapArray.size)
		if coord[1] == i
			leftStr = ""
			rightStr = ""
			if coord[0] > 0
				leftStr = mapArray[i][0..(coord[0] - 1)]
			end
			if coord[0] < (mapArray[i].size - 1)
				rightStr = mapArray[i][(coord[0] + 1)..-1]
			end
		puts (leftStr + player + rightStr)
		else
		puts mapArray[i]
		end
	end
end

while true
	showMap aArray, location, pSymbol
	#user movement inputs
	input = gets.chomp
	case input
	when "a"
		if location[0] > 0
			location[0] -= 1
		else
			puts "I cannot go any further left"
		end
	when "s"
		location[1] += 1
	when "d"
		location[0] += 1
	when "w"
		location[1] -= 1
	when "x"
		break
	else
		puts "what are you doing?"
	end
end

puts "you quit the game"
