#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(\+\d+|\w+)\] \[to:(\+\d+|\w+)\] \[flags:([-0-9:]+)\]/).join(",")
