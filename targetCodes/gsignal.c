//gsignal
#include <signal.h>
#include <stdint.h>
int target(uint8_t **data) {
	gsignal(data[0][0]);
	return 0;
}