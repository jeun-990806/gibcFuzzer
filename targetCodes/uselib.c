//uselib
#include <unistd.h>
#include <stdint.h>
int target(uint8_t **data) {
	uselib(data[0]);
	return 0;
}