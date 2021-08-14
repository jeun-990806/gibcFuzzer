//pvalloc
#include <malloc.h>
#include <stdint.h>
int target(uint8_t **data) {
	pvalloc(data[0][0]);
	return 0;
}