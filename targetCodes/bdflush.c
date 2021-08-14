//bdflush
#include <sys/kdaemon.h>
#include <stdint.h>
int target(uint8_t **data) {
	bdflush(data[0][0], data[1]);
	return 0;
}