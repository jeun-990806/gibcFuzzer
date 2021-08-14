//sgetspent
#include <shadow.h>
#include <stdint.h>
int target(uint8_t **data) {
	sgetspent(data[0]);
	return 0;
}