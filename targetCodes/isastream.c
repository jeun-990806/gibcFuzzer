//isastream
#include <stropts.h>
#include <stdint.h>
int target(uint8_t **data) {
	isastream(data[0][0]);
	return 0;
}