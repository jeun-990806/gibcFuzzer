//chroot
#include <unistd.h>
#include <stdint.h>
int target(uint8_t **data) {
	chroot(data[0]);
	return 0;
}