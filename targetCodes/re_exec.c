//re_exec
#include <sys/types.h>
#include <regex.h>
#include <stdint.h>
int target(uint8_t **data) {
	re_exec(data[0]);
	return 0;
}