//malloc_trim
#include <malloc.h>
#include <stdint.h>
int target(uint8_t **data) {
	malloc_trim(data[0][0]);
	return 0;
}