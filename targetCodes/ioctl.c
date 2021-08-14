//ioctl
#include <stropts.h>
#include <stdint.h>
int target(uint8_t **data) {
	ioctl(data[0][0], data[1][0]);
	return 0;
}