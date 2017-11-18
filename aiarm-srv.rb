#!/usr/bin/ruby
# encoding: utf-8

require 'sinatra'

configure do
  set :bind, '0.0.0.0'
end

get "/" do
  STDERR.puts params.inspect
  "Hello, Sinatra\n" + params.inspect

end


