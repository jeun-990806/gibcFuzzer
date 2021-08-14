//dlclose
#include <dlfcn.h>
#include <stdint.h>
int target(uint8_t **data) {
	dlclose(data[0]);
	return 0;
}