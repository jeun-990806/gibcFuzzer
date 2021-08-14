//feenableexcept
#include <fenv.h>
#include <stdint.h>
int target(uint8_t **data) {
	feenableexcept(data[0][0]);
	return 0;
}