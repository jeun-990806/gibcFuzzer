//openat
#include <sys/stat.h>
#include <fcntl.h>
#include <stdint.h>
int target(uint8_t **data) {
	openat(data[0][0], data[1], data[2][0]);
	return 0;
}