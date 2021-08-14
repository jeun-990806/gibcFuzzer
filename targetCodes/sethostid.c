//sethostid
#include <unistd.h>
#include <stdint.h>
int target(uint8_t **data) {
	sethostid(data[0][0]);
	return 0;
}