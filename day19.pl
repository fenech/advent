#!/usr/bin/env perl

# not my code!
# https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/

use strict;
use warnings;

my %rule = map { reverse =~ m/(\w*).*\b(\w+)/ } <>;
my $string = delete $rule{""};
my $count = 0; $count++ while ($string =~ s/(@{[ join "|", keys %rule ]})/$rule{$1}/);
print "$count @{[scalar reverse $string]}\n";
