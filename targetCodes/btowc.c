//btowc
#include <wchar.h>
#include <stdint.h>
int target(uint8_t **data) {
	btowc(data[0][0]);
	return 0;
}