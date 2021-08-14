//feraiseexcept
#include <fenv.h>
#include <stdint.h>
int target(uint8_t **data) {
	feraiseexcept(data[0][0]);
	return 0;
}