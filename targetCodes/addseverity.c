//addseverity
#include <fmtmsg.h>
#include <stdint.h>
int target(uint8_t **data) {
	addseverity(data[0][0], data[1]);
	return 0;
}