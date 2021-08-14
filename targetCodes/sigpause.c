//sigpause
#include <signal.h>
#include <stdint.h>
int target(uint8_t **data) {
	sigpause(data[0][0]);
	return 0;
}