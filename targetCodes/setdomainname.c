//setdomainname
#include <unistd.h>
#include <stdint.h>
int target(uint8_t **data) {
	setdomainname(data[0], data[1][0]);
	return 0;
}