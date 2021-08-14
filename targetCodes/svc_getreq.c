//svc_getreq
#include <rpc/rpc.h>
#include <stdint.h>
int target(uint8_t **data) {
	svc_getreq(data[0][0]);
	return 0;
}