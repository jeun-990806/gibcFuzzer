//passwd2des
#include <rpc/des_crypt.h>
#include <stdint.h>
int target(uint8_t **data) {
	passwd2des(data[0], data[1]);
	return 0;
}