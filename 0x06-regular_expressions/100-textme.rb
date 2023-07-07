#!/usr/bin/env ruby
# This script should output: [SENDER],[RECEIVER],[FLAGS]
# The sender phone number or name (including country code if present)
# The receiver phone number or name (including country code if present)
# The flags that were used

puts ARGV[0].scan(/\[from:(\+?\w*)\]\s\[to:(\+?\w*)\]\s\[flags:(\S*)\]/).join(',')
