//brk
#include <unistd.h>
#include <stdint.h>
int target(uint8_t **data) {
	brk(data[0]);
	return 0;
}