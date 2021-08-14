//malloc_usable_size
#include <malloc.h>
#include <stdint.h>
int target(uint8_t **data) {
	malloc_usable_size(data[0]);
	return 0;
}