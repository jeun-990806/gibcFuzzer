//svcudp_create
#include <rpc/rpc.h>
#include <stdint.h>
int target(uint8_t **data) {
	svcudp_create(data[0][0]);
	return 0;
}