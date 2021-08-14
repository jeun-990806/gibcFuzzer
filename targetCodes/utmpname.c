//utmpname
#include <utmp.h>
#include <stdint.h>
int target(uint8_t **data) {
	utmpname(data[0]);
	return 0;
}