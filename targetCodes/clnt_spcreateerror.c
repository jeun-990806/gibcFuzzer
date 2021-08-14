//clnt_spcreateerror
#include <rpc/rpc.h>
#include <stdint.h>
int target(uint8_t **data) {
	clnt_spcreateerror(data[0]);
	return 0;
}