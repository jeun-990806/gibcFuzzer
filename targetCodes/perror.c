//perror
#include <stdio.h>
#include <stdint.h>
int target(uint8_t **data) {
	perror(data[0]);
	return 0;
}