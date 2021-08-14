//sighold
#include <signal.h>
#include <stdint.h>
int target(uint8_t **data) {
	sighold(data[0][0]);
	return 0;
}