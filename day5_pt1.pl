#!/usr/bin/env perl

while (<>) {
    my @m = ($_ =~ /[aeiou]/g);
    if (@m ge 3 && /(.)\1/ && !/ab|cd|pq|xy/) {
	++$count;
    }
}

print "$count\n";
