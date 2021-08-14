//fetestexcept
#include <fenv.h>
#include <stdint.h>
int target(uint8_t **data) {
	fetestexcept(data[0][0]);
	return 0;
}