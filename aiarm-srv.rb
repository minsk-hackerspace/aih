#!/usr/bin/ruby
# encoding: utf-8

require 'sinatra'
require './anims.rb'


$server = '100.45.255.181:8080'

$server = ARGV[0] unless ARGV.empty?


ACTIONS = {
  'beer' => [:loork, :no],
  'пивка' => [:loork, :no],
  'пива' => [:loork, :no],
  'привет' => [:greet],
  'hello' => [:greet],
  'брось' => [:drop],
  'кинь' => [:drop],
  'drop' => [:drop],
  'клац' => [:klac],
  'клац-клац' => [:klac,:klac],
  'банан' => [:loork, :get_10_0],
  'banan' => [:loork, :get_10_0],
  'яблоко' => [:loork, :get_15__13],
  'apple' => [:loork, :get_15__13],
  'hugg' => [:hugg],
  'обними' => [:hugg],
  'обнимашки' => [:hugg],
}

$anims = RoboAnims.new(server: $server)
$busy = false

def do_actions(actions)
  actions.each do |a|
    STDERR.puts "Sending #{a}"
    $anims.send a
  end
end


configure do
  set :bind, '0.0.0.0'
end

get "/" do

  STDERR.puts params.inspect

  unless $busy
    $busy = true
    params[:t].split(' ').each do |word|
      word.downcase!
      STDERR.puts "Handling #{word}..."
      do_actions ACTIONS[word] unless ACTIONS[word].nil?
    end
    $busy = false
  else
    STDERR.puts "Don't run – arm busy"
  end

  params.inspect

end


