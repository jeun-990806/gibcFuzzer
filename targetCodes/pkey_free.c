//pkey_free
#include <sys/mman.h>
#include <stdint.h>
int target(uint8_t **data) {
	pkey_free(data[0][0]);
	return 0;
}