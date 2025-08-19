#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
  time_t t; time(&t);

  // HTTP 头
  printf("Cache-Control: no-cache\n");
  printf("Content-type: text/html\n\n");

  // HTML
  printf("<html><head><title>Hello, C!</title></head><body>");
  printf("<h1 align='center'>Yanhua Liu was here - Hello, C!</h1><hr/>");
  printf("This page was generated with the C language<br/>\n");
  printf("Current Time: %s<br/>\n", ctime(&t));
  printf("Your current IP address is: %s<br/>\n", getenv("REMOTE_ADDR"));
  printf("</body></html>");
  return 0;
}
