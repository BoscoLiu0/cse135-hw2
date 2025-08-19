#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv, char **envp)
{
  printf("Cache-Control: no-cache\n");
  printf("Set-Cookie: destroyed\n");
  printf("Content-type: text/html\n\n");

  printf("<html><head><title>C Session Destroyed</title></head><body>");
  printf("<h1>C Session Destroyed</h1>");
  printf("<a href=\"/cgi-bin/c-sessions-1.cgi\">Back to Page 1</a><br />");
  printf("<a href=\"/cgi-bin/c-sessions-2.cgi\">Back to Page 2</a><br />");
  printf("<a href=\"/c-cgiform.html\">C CGI Form</a>");
  printf("</body></html>");
  return 0;
}
