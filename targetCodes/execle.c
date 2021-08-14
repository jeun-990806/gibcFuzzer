//execle
#include <unistd.h>
#include <stdint.h>
int target(uint8_t **data) {
	execle(data[0], data[1]);
	return 0;
}