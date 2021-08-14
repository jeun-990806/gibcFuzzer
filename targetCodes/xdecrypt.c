//xdecrypt
#include <rpc/des_crypt.h>
#include <stdint.h>
int target(uint8_t **data) {
	xdecrypt(data[0], data[1]);
	return 0;
}