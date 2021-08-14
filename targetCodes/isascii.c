//isascii
#include <ctype.h>
#include <stdint.h>
int target(uint8_t **data) {
	isascii(data[0][0]);
	return 0;
}