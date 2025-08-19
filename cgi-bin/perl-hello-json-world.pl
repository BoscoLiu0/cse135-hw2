#!/usr/bin/perl
use JSON;
print "Cache-Control: no-cache\n";
print "Content-type: application/json\n\n";
my $date = localtime();
my $address = $ENV{REMOTE_ADDR};
my %message = (
  title   => 'Hello, Perl!',
  heading => 'Hello, Perl!',
  message => 'This page was generated with the Perl programming language',
  time    => $date,
  IP      => $address,
  note    => 'Yanhua Liu was here'
);
print encode_json(\%message), "\n";
