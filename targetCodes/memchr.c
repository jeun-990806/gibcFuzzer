//memchr
#include <string.h>
#include <stdint.h>
int target(uint8_t **data) {
	memchr(data[0], data[1][0], data[2][0]);
	return 0;
}