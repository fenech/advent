#!/usr/bin/env perl

while (<>) {
    ++$count if (/(..).*\1/ && /(.).\1/);
}

print "$count\n";
