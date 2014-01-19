#/ Usage: ruby talk.rb

require 'socket'

r,w = IO.pipe
running = true
[:INT, :TERM, :QUIT].each { |sig| trap(sig) { running = false ; w << '.' } }

socket = UDPSocket.new
socket.bind('', 4576)
while running
  rs, ws = IO.select([socket, r])
  if rs.include?(socket)
    message, sender = socket.recvfrom(1024)
    p [message, sender]
    system "say", "hello hello hello i'm the one who loves you so"
  end
end
