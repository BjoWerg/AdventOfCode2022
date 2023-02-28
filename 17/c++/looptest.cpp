#include <iostream>

using namespace std;

int main()
{

    bool sfere[10][3][5];

    int x_len = sizeof(sfere)/sizeof(sfere[0]);
    int y_len = sizeof(sfere[0])/sizeof(sfere[0][0]);
    int z_len = sizeof(sfere[0][0])/sizeof(bool);
    printf("[%d][%d][%d]",x_len,y_len,z_len);
/*    const uint64_t last_rock = 1000000000000;
    uint64_t rock_nbr = 0;

    while (rock_nbr < last_rock) {
        if ((rock_nbr%100000000) == 0) {
            printf(" --- %llu ---\r", rock_nbr/1000000);
        }
        rock_nbr += 1;
    }
    printf("\ntop is at %llu", rock_nbr);
*/

    return 0;
} 