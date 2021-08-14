//dlvsym
#include <dlfcn.h>
#include <stdint.h>
int target(uint8_t **data) {
	dlvsym(data[0], data[1], data[2]);
	return 0;
}