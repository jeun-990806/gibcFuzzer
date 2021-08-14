//strfmon
#include <monetary.h>
#include <stdint.h>
int target(uint8_t **data) {
	strfmon(data[0], data[1][0], data[2]);
	return 0;
}