#include <stdio.h>
#include <time.h>

int main() {
    time_t timestamp;
    time(&timestamp);
    printf("Current timestamp: %ld\n", (long)timestamp);
    return 0;
}
