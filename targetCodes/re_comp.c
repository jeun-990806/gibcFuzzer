//re_comp
#include <sys/types.h>
#include <regex.h>
#include <stdint.h>
int target(uint8_t **data) {
	re_comp(data[0]);
	return 0;
}