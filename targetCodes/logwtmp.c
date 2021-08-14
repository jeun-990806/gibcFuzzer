//logwtmp
#include <utmp.h>
#include <stdint.h>
int target(uint8_t **data) {
	logwtmp(data[0], data[1], data[2]);
	return 0;
}