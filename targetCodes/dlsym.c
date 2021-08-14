//dlsym
#include <dlfcn.h>
#include <stdint.h>
int target(uint8_t **data) {
	dlsym(data[0], data[1]);
	return 0;
}