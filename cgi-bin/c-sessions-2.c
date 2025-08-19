#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv, char **envp)
{
  printf("Cache-Control: no-cache\n");
  printf("Content-type: text/html\n\n");

  printf("<html><head><title>C Sessions</title></head><body>");
  printf("<h1>C Sessions Page 2</h1><table>");

  if (getenv("HTTP_COOKIE") != NULL && strcmp(getenv("HTTP_COOKIE"), "destroyed")) {
    printf("<tr><td>Cookie:</td><td>%s</td></tr>\n", getenv("HTTP_COOKIE"));
  } else {
    printf("<tr><td>Cookie:</td><td>None</td></tr>\n");
  }

  printf("</table><br />");
  printf("<a href=\"/cgi-bin/c-sessions-1.cgi\">Session Page 1</a><br />");
  printf("<a href=\"/c-cgiform.html\">C CGI Form</a><br /><br />");
  printf("<form action=\"/cgi-bin/c-destroy-session.cgi\" method=\"get\">");
  printf("<button type=\"submit\">Destroy Session</button>");
  printf("</form>");
  printf("</body></html>");
  return 0;
}
