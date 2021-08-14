//key_setsecret
#include <rpc/rpc.h>
#include <stdint.h>
int target(uint8_t **data) {
	key_setsecret(data[0]);
	return 0;
}