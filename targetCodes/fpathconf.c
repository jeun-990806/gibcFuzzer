//fpathconf
#include <unistd.h>
#include <stdint.h>
int target(uint8_t **data) {
	fpathconf(data[0][0], data[1][0]);
	return 0;
}