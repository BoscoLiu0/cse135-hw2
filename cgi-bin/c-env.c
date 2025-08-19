#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv, char **envp) {
  printf("Cache-Control: no-cache\n");
  printf("Content-type: text/html\n\n");
  printf("<html><head><title>Environment Variables</title></head>");
  printf("<body><h1 align='center'>Environment Variables</h1><hr/>\n");

  for (char **env = envp; *env != NULL; env++) {
    printf("%s<br/>\n", *env);
  }

  printf("</body></html>");
  return 0;
}
