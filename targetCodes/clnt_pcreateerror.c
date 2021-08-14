//clnt_pcreateerror
#include <rpc/rpc.h>
#include <stdint.h>
int target(uint8_t **data) {
	clnt_pcreateerror(data[0]);
	return 0;
}