#!/usr/bin/perl
use CGI;
use CGI::Session;

my $session = CGI::Session->new("driver:File", undef, {Directory=>"/tmp"});
my $cgi = CGI->new;

# 用 CGISESSID 这一个 cookie 名
my $cookie = $cgi->cookie(CGISESSID => $session->id);
print $cgi->header(-cookie=>$cookie);

my $name = $session->param('username') || $cgi->param('username');
$session->param("username", $name) if defined $name;

print "<html><head><title>Perl Sessions</title></head><body>";
print "<h1>Perl Sessions Page 1</h1>";
if ($session->param('username')){
  print "<p><b>Name:</b> ".$session->param('username')."</p>";
}else{
  print "<p><b>Name:</b> You do not have a name set</p>";
}
print qq{
  <br/><br/>
  <a href="/cgi-bin/perl-sessions-2.pl">Session Page 2</a><br/>
  <a href="/perl-cgiform.html">Perl CGI Form</a><br/>
  <form style="margin-top:30px" action="/cgi-bin/perl-destroy-session.pl" method="get">
    <button type="submit">Destroy Session</button>
  </form>
</body></html>
};
