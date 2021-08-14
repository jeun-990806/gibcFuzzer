//dlopen
#include <dlfcn.h>
#include <stdint.h>
int target(uint8_t **data) {
	dlopen(data[0], data[1][0]);
	return 0;
}