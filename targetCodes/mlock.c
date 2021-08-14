//mlock
#include <sys/mman.h>
#include <stdint.h>
int target(uint8_t **data) {
	mlock(data[0], data[1][0]);
	return 0;
}