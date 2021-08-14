//syslog
#include <syslog.h>
#include <stdint.h>
int target(uint8_t **data) {
	syslog(data[0][0], data[1]);
	return 0;
}