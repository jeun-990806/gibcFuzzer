//if_nametoindex
#include <net/if.h>
#include <stdint.h>
int target(uint8_t **data) {
	if_nametoindex(data[0]);
	return 0;
}