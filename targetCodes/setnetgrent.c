//setnetgrent
#include <netdb.h>
#include <stdint.h>
int target(uint8_t **data) {
	setnetgrent(data[0]);
	return 0;
}