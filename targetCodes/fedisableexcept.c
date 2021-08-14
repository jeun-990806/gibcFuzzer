//fedisableexcept
#include <fenv.h>
#include <stdint.h>
int target(uint8_t **data) {
	fedisableexcept(data[0][0]);
	return 0;
}