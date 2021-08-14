//execl
#include <unistd.h>
#include <stdint.h>
int target(uint8_t **data) {
	execl(data[0], data[1]);
	return 0;
}