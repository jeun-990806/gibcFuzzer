//feclearexcept
#include <fenv.h>
#include <stdint.h>
int target(uint8_t **data) {
	feclearexcept(data[0][0]);
	return 0;
}