#!/usr/bin/perl
use CGI;
use CGI::Session;

my $cgi = CGI->new;
my $session = CGI::Session->new(undef, $cgi, {Directory=>'/tmp'});

print "Content-Type: text/html\n\n";
print "<html><head><title>Perl Sessions</title></head><body>";
print "<h1>Perl Sessions Page 2</h1>";

my $name = $session->param("username");
if ($name){
  print "<p><b>Name:</b> $name</p>";
}else{
  print "<p><b>Name:</b> You do not have a name set</p>";
}
print qq{
  <br/><br/>
  <a href="/cgi-bin/perl-sessions-1.pl">Session Page 1</a><br/>
  <a href="/perl-cgiform.html">Perl CGI Form</a><br/>
  <form style="margin-top:30px" action="/cgi-bin/perl-destroy-session.pl" method="get">
    <button type="submit">Destroy Session</button>
  </form>
</body></html>
};
