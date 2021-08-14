//getdate
#include <time.h>
#include <stdint.h>
int target(uint8_t **data) {
	getdate(data[0]);
	return 0;
}