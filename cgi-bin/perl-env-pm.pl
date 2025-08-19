#!/usr/bin/perl
use CGI qw/:standard/;
print "Cache-Control: no-cache\n";
print header;
print start_html("Environment Variables");
print "<h1 align='center'>Environment Variables</h1><hr />";
for my $k (sort keys %ENV){ print "$k = $ENV{$k}<br />\n"; }
print end_html;
