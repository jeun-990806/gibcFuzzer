//timerfd_create
#include <sys/timerfd.h>
#include <stdint.h>
int target(uint8_t **data) {
	timerfd_create(data[0][0], data[1][0]);
	return 0;
}