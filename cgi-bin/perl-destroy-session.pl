#!/usr/bin/perl
use CGI;
use CGI::Session;

print "Content-type: text/html\n\n";
my $cgi = CGI->new;
my $session = CGI::Session->new(undef, $cgi, {Directory=>'/tmp'});
$session->delete();

print "<html><head><title>Perl Session Destroyed</title></head><body>";
print "<h1>Session Destroyed</h1>";
print q{
  <a href="/perl-cgiform.html">Back to the Perl CGI Form</a><br/>
  <a href="/cgi-bin/perl-sessions-1.pl">Back to Page 1</a><br/>
  <a href="/cgi-bin/perl-sessions-2.pl">Back to Page 2</a>
</body></html>
};
