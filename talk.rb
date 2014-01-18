#/ Usage: ruby talk.rb

require 'sinatra'

set :port, 4576

post '/talk' do
  system 'say hello raspberry pi'
  'ok'
end

get /.*/ do
  content_type :text
  "Try this:\n$ curl -X POST http://#{`hostname`}/talk\n"
end
