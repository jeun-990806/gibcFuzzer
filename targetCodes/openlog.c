//openlog
#include <syslog.h>
#include <stdint.h>
int target(uint8_t **data) {
	openlog(data[0], data[1][0], data[2][0]);
	return 0;
}