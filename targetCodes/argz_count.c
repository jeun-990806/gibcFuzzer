//argz_count
#include <argz.h>
#include <stdint.h>
int target(uint8_t **data) {
	argz_count(data[0], data[1][0]);
	return 0;
}