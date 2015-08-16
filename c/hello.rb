#!/usr/bin/env ruby

def help_msg()
	puts "'h' go left"
	puts "'l' go right"
	puts "'?' this help message"
	puts "'q' quit"
end

def room_msg(x)
  puts "you are in room #{x}"
end

room = 0
game_loop = true

help_msg()
room_msg(room)

while game_loop do
  case gets.chomp
  when 'h'
    room -= 1
    room_msg(room)
  when 'l'
    room += 1
    room_msg(room)
  when '?'
    help_msg()
  when 'q'
    game_loop = false
  else
    # do nothing
  end
end

puts "thanks for playing"
