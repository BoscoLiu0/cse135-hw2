#!/usr/bin/perl
print "Cache-Control: no-cache\n";
print "Content-type: text/html\n\n";
print "<html><head><title>Hello, Perl!</title></head><body>";
print "<h1>Yanhua Liu was here - Hello, Perl!</h1>";
print "<p>This page was generated with the Perl programming language</p>";
my $date = localtime();
print "<p>Current Time: $date</p>";
my $address = $ENV{REMOTE_ADDR};
print "<p>Your IP Address: $address</p>";
print "</body></html>";
