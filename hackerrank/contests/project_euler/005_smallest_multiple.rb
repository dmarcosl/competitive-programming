#!/bin/ruby

(0..gets.strip.to_i-1).each{|_| puts (1..gets.strip.to_i).reduce(1){|prod, i| i.lcm(prod)}}

