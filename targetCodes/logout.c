//logout
#include <utmp.h>
#include <stdint.h>
int target(uint8_t **data) {
	logout(data[0]);
	return 0;
}