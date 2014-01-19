#/ Usage: ruby talk.rb

require 'socket'

r,w = IO.pipe
running = true
[:INT, :TERM, :QUIT].each { |sig| trap(sig) { running = false ; w << '.' } }

thing_to_say = ARGV
thing_to_say = ['good day!'] if thing_to_say.empty?

socket = UDPSocket.new
socket.bind('', 4576)
while running
  rs, ws = IO.select([socket, r])
  if rs.include?(socket)
    message, sender = socket.recvfrom(1024)
    system "say", *thing_to_say
  end
end
