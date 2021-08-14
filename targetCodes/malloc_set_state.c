//malloc_set_state
#include <malloc.h>
#include <stdint.h>
int target(uint8_t **data) {
	malloc_set_state(data[0]);
	return 0;
}