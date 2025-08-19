#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int main(void) {
  time_t t; time(&t);
  char *buf = ctime(&t);
  if (buf) { buf[strlen(buf)-1] = '\0'; } // 去掉结尾换行

  printf("Cache-Control: no-cache\r\n");
  printf("Content-type: application/json\r\n\r\n");
  printf("{\n");
  printf("  \"message\": \"Hello, C (JSON)!\",\n");
  printf("  \"note\": \"Yanhua Liu was here\",\n");
  printf("  \"date\": \"%s\",\n", buf ? buf : "");
  printf("  \"currentIP\": \"%s\"\n", getenv("REMOTE_ADDR"));
  printf("}\n");
  return 0;
}
