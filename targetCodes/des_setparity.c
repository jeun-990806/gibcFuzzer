//des_setparity
#include <rpc/des_crypt.h>
#include <stdint.h>
int target(uint8_t **data) {
	des_setparity(data[0]);
	return 0;
}