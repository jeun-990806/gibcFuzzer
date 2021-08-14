//getwd
#include <unistd.h>
#include <stdint.h>
int target(uint8_t **data) {
	getwd(data[0]);
	return 0;
}