#!/usr/bin/ruby
# encoding: utf-8

require 'sinatra'

get "/" do
  STDERR.puts params.inspect
  "Hello, Sinatra\n" + params.inspect

end


