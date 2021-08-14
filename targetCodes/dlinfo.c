//dlinfo
#include <link.h>
#include <dlfcn.h>
#include <stdint.h>
int target(uint8_t **data) {
	dlinfo(data[0], data[1][0], data[2]);
	return 0;
}