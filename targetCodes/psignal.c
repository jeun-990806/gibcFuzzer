//psignal
#include <signal.h>
#include <stdint.h>
int target(uint8_t **data) {
	psignal(data[0][0], data[1]);
	return 0;
}