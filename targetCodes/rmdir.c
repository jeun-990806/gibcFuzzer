//rmdir
#include <unistd.h>
#include <stdint.h>
int target(uint8_t **data) {
	rmdir(data[0]);
	return 0;
}