#!/usr/bin/perl
print "Cache-Control: no-cache\n";
print "Content-type: text/html\n\n";
print "<!DOCTYPE html><html><head><title>Environment Variables</title></head>";
print "<body><h1 align='center'>Environment Variables</h1><hr>";
for my $k (sort keys %ENV){ print "<b>$k:</b> $ENV{$k}<br/>\n"; }
print "</body></html>";
