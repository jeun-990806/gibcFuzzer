//unlink
#include <unistd.h>
#include <stdint.h>
int target(uint8_t **data) {
	unlink(data[0]);
	return 0;
}