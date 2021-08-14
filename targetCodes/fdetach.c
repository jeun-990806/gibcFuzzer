//fdetach
#include <stropts.h>
#include <stdint.h>
int target(uint8_t **data) {
	fdetach(data[0]);
	return 0;
}