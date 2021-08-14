//argz_stringify
#include <argz.h>
#include <stdint.h>
int target(uint8_t **data) {
	argz_stringify(data[0], data[1][0], data[2][0]);
	return 0;
}