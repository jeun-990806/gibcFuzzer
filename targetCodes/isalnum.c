//isalnum
#include <ctype.h>
#include <stdint.h>
int target(uint8_t **data) {
	isalnum(data[0][0]);
	return 0;
}