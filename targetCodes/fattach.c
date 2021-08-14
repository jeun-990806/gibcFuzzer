//fattach
#include <stropts.h>
#include <stdint.h>
int target(uint8_t **data) {
	fattach(data[0][0], data[1]);
	return 0;
}