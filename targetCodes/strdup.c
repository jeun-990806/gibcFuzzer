//strdup
#include <string.h>
#include <stdint.h>
int target(uint8_t **data) {
	strdup(data[0]);
	return 0;
}