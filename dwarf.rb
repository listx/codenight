#!/usr/bin/env ruby

map = "0123456789"
location = 0
teleports = 3
monsters = []

class Creature
  def initialize name, coord
    @name = name
    @asleep = false
    @health     = 10  #  He's full.
    @mana	= 10
    @stamina	= 10
    @coord = coord
#    puts @name + ' is born.'
  end

  def name
    @name
  end

  def coord
    @coord
  end

  private

  #  "private" means that the methods defined here are
  #  methods internal to the object.  (You can feed
  #  your dragon, but you can't ask him if he's hungry.)

#  def hungry?
#    #  Method names can end with "?".
#    #  Usually, we only do this if the method
#    #  returns true or false, like this:
#    @stuffInBelly <= 2
#  end
end

def show_location (mapstr, coord)
  left = ""
  right = ""
  if coord > 0
    left = mapstr[0..(coord - 1)]
  end

  if coord < (mapstr.size - 1)
    right = mapstr[(coord + 1)..-1]
  end

  puts "\n#{left}@#{right}"
end

def show_monsters (monsters_list, coord)
  monsters_list.each do |m|
    if m.coord == coord
      puts "#{m.name} is here"
    end
  end
end

def in_range (idx, str)
  if idx >= 0 && idx < str.size
    true
  else
    false
  end
end

while true
  show_location map, location
  show_monsters monsters, location
  puts "you are in room #{map[location]}"
  puts "you have #{teleports} teleportation spells left"
  input = gets.chomp
  teleports_regen = false
#  puts input # debug
  case input
  when "e", "east"
    if (location < map.size - 1)
      puts "you go east..."
      location += 1
    else
      puts "sorry, you can't go there"
    end
    teleports_regen = true
  when "w", "west"
    if (location > 0)
      puts "you go west..."
      location -= 1
    else
      puts "sorry, you can't go there"
    end
    teleports_regen = true
  when /^\s*tel\s*\d+\s*$/ # "tel343244"
    roomNum = input.match(/(?<room_number>\d+)/)[:room_number].to_i
    if (in_range roomNum, map) && teleports > 0
      puts "you teleport to #{roomNum}..."
      location = roomNum
      teleports -= 1
      monsters << (Creature.new "MONSTER", roomNum)
    else
      if teleports < 1
        puts "you ran out of teleport spells"
      else
        puts "you cannot teleport there"
      end
    end
  when "quit", "q", "exit"
    break
  else
    puts "wtf is ``#{input}''?!?!"
  end
  if teleports_regen && teleports < 3
    teleports += 1
  end
end

puts "goodbye!"
