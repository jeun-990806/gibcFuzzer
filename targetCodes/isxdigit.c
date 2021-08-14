//isxdigit
#include <ctype.h>
#include <stdint.h>
int target(uint8_t **data) {
	isxdigit(data[0][0]);
	return 0;
}