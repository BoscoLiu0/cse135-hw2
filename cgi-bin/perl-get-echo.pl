#!/usr/bin/perl
print "Cache-Control: no-cache\n";
print "Content-type: text/html\n\n";
print "<!DOCTYPE html><html><head><title>GET Request Echo</title></head>";
print "<body><h1 align='center'>Get Request Echo</h1><hr>";
print "<b>Query String:</b> $ENV{QUERY_STRING}<br/>\n";
my %in;
if (length $ENV{QUERY_STRING}) {
  my $buffer = $ENV{QUERY_STRING};
  my @pairs = split /&/, $buffer;
  for my $pair (@pairs){
    my ($name,$value)=split /=/, $pair;
    $value =~ s/%([a-fA-F0-9]{2})/pack("C",hex($1))/eg;
    $in{$name} = $value;
  }
}
my $i=0;
for my $k (%in){ $i++; print "$k = $in{$k}<br/>\n" if $i%2; }
print "</body></html>";
