#!/usr/bin/perl
print "Cache-Control: no-cache\n";
print "Content-type: text/html\n\n";
print "<!DOCTYPE html><html><head><title>POST Request Echo</title></head>";
print "<body><h1 align='center'>POST Request Echo</h1><hr>";
my $bytes_read = read STDIN, my $form_data, $ENV{CONTENT_LENGTH};
my %in;
if (length $form_data){
  my @pairs = split /&/, $form_data;
  for my $pair (@pairs){
    my ($name,$value)=split /=/, $pair;
    $value =~ s/%([a-fA-F0-9]{2})/pack("C",hex($1))/eg;
    $in{$name} = $value;
  }
}
print "<b>Message Body:</b><br/><ul>\n";
my $i=0;
for my $k (%in){ $i++; print "<li>$k = $in{$k}</li>\n" if $i%2; }
print "</ul></body></html>\n";
