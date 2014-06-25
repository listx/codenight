#!/usr/bin/env ruby

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

def loadmap filename
  maptext = []
  file = File.open(filename, "r")
  file.each_line do |line|
    maptext << line
  end
  reference_size = maptext[0].size
  maptext.each do |line|
    if line.size != reference_size
      puts "import map: error!!! (non uniform line lengths)"
      return false
    end
  end
  true
end

while true
  importOk = loadmap "cmap"
  if !importOk
    puts "map import failure"
    exit
  end
  exit
	showMap aArray, location, pSymbol
	#user movement inputs
	input = gets.chomp
	case input
	when "w", "west"
		if location[0] > 0
			location[0] -= 1
		else
			puts "I cannot go any further west"
		end
	when "s", "south"
		if location[1] < (aArray.size - 1)
			location[1] += 1
		else
			puts "I cannot go any further south"
		end
	when "e", "east"
		if location[0] < (aArray[0].size - 1)
                        location[0] += 1
		else
			puts "I cannot go any further east"
		end
	when "n", "north"
		if location[1] > 0
			location[1] -= 1
		else
			puts "I cannot go any further north"
		end
	when "x"
		break
	else
		puts "what are you doing?"
	end
end

puts "you quit the game"
