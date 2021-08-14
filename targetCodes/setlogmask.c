//setlogmask
#include <syslog.h>
#include <stdint.h>
int target(uint8_t **data) {
	setlogmask(data[0][0]);
	return 0;
}