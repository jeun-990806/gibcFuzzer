//isprint
#include <ctype.h>
#include <stdint.h>
int target(uint8_t **data) {
	isprint(data[0][0]);
	return 0;
}