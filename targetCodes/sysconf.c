//sysconf
#include <unistd.h>
#include <stdint.h>
int target(uint8_t **data) {
	sysconf(data[0][0]);
	return 0;
}