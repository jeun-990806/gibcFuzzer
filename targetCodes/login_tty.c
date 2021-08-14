//login_tty
#include <utmp.h>
#include <stdint.h>
int target(uint8_t **data) {
	login_tty(data[0][0]);
	return 0;
}