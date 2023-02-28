#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

int main()
{
    string direction;
    ifstream inputfile; 

    direction = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>";
//    inputfile.open("input17.txt");
//    inputfile >> direction;
//    inputfile.close();

    int d_length = direction.length();
    int d_index = 0;

     const int last_rock = 2022;
//const uint64_t last_rock = 1000000000000ULL;

    const int num_rocks = 5;
    const uint32_t rocks[] = {
        0b00000000000000000000000000111100,\
        0b00000000000100000011100000010000,\
        0b00000000000010000000100000111000,\
        0b00100000001000000010000000100000,\
        0b00000000000000000011000000110000
    };
    const int r_hight[] = {0,2,2,3,1};

    const uint32_t left_wall = 0b10000000100000001000000010000000;
    const uint32_t right_wall = 0b00000010000000100000001000000010;

    const int t_length = 1000;
    uint8_t tower[t_length+4];
    memset(tower, 0, t_length);
    tower[0] = 0b11111111;

    uint64_t rock_nbr = 0;
    uint64_t top = 0;
    printf(" --- %llu ---\r", rock_nbr);

    while (rock_nbr < last_rock) {
        uint32_t rock = rocks[rock_nbr%num_rocks];
        uint64_t row = top+4;
        bool falling = true;
        uint32_t tower_tmp = 0;

        if ((rock_nbr%100000000) == 0) {
            printf(" --- %llu ---\r", rock_nbr/1000000ULL);
        }

        memset(&tower[(top+1)%t_length], 0, 4);

        while (falling) {
            if (direction[d_index] == '<') {
                if ((rock&left_wall) == 0) {
                    rock <<= 1;
                    if (row<=top) {
                        if ((rock & *((uint32_t*)(&tower[row%t_length]))) != 0) {
                            rock >>= 1;
                        }
                    }
                }
            } else {
                if ((rock&right_wall) == 0) {
                    rock >>= 1;
                    if (row<=top) {
                        if ((rock & *((uint32_t*)(&tower[row%t_length]))) != 0) {
                            rock <<= 1;
                        }
                    }
                }
            }
            d_index = (d_index+1)%d_length;

            row -= 1;
            if (row<=top) {
                if ((rock & *((uint32_t*)(&tower[row%t_length]))) != 0) {
                    row += 1;
                    falling = false;
                }
            }
        }

        rock |= *((uint32_t*)(&tower[row%t_length]));
        memcpy(&tower[row%t_length], (uint8_t*)&rock, 4);
        int space = t_length-(row%t_length);
        if (space < 4) {
            rock >>= space*8;
            memcpy(tower, (uint8_t*)&rock, 4-space);
        }
        if ((row+r_hight[rock_nbr%num_rocks]) > top) {
            top = row+r_hight[rock_nbr%num_rocks];
        }
        rock_nbr += 1;
/* Print the tower 
        printf("\n");
       	for (int i=top; i>=0; i--) {
            for (int j=7; j>=0; j--) {
                printf("%d",(tower[i%t_length]>>j)&1);
            }
            printf("\n");
        }
        printf("\n");
*/
    }
    
    printf("top is at %llu", top);

    return 0;
}