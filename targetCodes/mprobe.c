//mprobe
#include <mcheck.h>
#include <stdint.h>
int target(uint8_t **data) {
	mprobe(data[0]);
	return 0;
}