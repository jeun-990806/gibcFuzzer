//link
#include <unistd.h>
#include <stdint.h>
int target(uint8_t **data) {
	link(data[0], data[1]);
	return 0;
}