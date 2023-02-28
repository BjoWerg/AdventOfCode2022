#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
#include <array>

using namespace std;

int main() {
    ifstream inputfile; 
    string str,temp;

    int x_max = 0;
    int y_max = 0;
    int z_max = 0;

    int cube[3000][3];
    int nbr_of_cubes = 0;
    inputfile.open("input18.txt");
    while (getline(inputfile, str))
    {
        stringstream ss = stringstream(str);
        int i = 0;
        while(getline(ss, temp,','))
        {
            stringstream(temp) >> cube[nbr_of_cubes][i++];
        }
        if (cube[nbr_of_cubes][0] > x_max) x_max = cube[nbr_of_cubes][0];
        if (cube[nbr_of_cubes][1] > y_max) y_max = cube[nbr_of_cubes][1];
        if (cube[nbr_of_cubes][2] > z_max) z_max = cube[nbr_of_cubes][2];
        nbr_of_cubes++;
    }
    inputfile.close();

    // Part 1
    int nbr_sides = 0;
    for (int i=0; i<nbr_of_cubes; i++)
    {
        int tmp_sides = 6;
        for (int j=0; j<nbr_of_cubes; j++)
        {
            if (((abs(cube[i][0]-cube[j][0]) == 1) && (cube[i][1] == cube[j][1]) && (cube[i][2] == cube[j][2])) ||
                ((abs(cube[i][1]-cube[j][1]) == 1) && (cube[i][2] == cube[j][2]) && (cube[i][0] == cube[j][0])) ||
                ((abs(cube[i][2]-cube[j][2]) == 1) && (cube[i][0] == cube[j][0]) && (cube[i][1] == cube[j][1])))
                tmp_sides--;
        }
        nbr_sides += tmp_sides;
    }
    printf("Number of open sides %d\n", nbr_sides);

    // Part 2
    x_max +=2;
    y_max +=2;
    z_max +=2;
    int cubes[x_max][y_max][z_max];
    for (int i=0; i<x_max;i++)
    {
        for (int j=0; j<y_max;j++)
        {
            for (int k=0; k<z_max;k++)
            {
                cubes[i][j][k] = 0;
            }
        }
    }

    for (int i=0; i<nbr_of_cubes; i++)
    {
        cubes[cube[i][0]][cube[i][1]][cube[i][2]] = 1;
    }

    nbr_sides = 0;
    vector<array<int,3>> list; 
    list.push_back({0, 0, 0});
    cubes[0][0][0] = 2;
    while (list.size() > 0)
    {
        array<int,3> c = list.front();
        
        if (c[0] > 0)
        {
            if (cubes[c[0]-1][c[1]][c[2]] == 1)
            {
                nbr_sides++;
            }
            else if (cubes[c[0]-1][c[1]][c[2]] == 0)
            {
                list.push_back({c[0]-1, c[1], c[2]});
                cubes[c[0]-1][c[1]][c[2]] = 2;
            }
        }
        if (c[0] < x_max-1)
        {
            if (cubes[c[0]+1][c[1]][c[2]] == 1)
            {
                nbr_sides++;
            }
            else if (cubes[c[0]+1][c[1]][c[2]] == 0)
            {
                list.push_back({c[0]+1, c[1], c[2]});
                cubes[c[0]+1][c[1]][c[2]] = 2;
            }
        }

        if (c[1] > 0)
        {
            if (cubes[c[0]][c[1]-1][c[2]] == 1)
            {
                nbr_sides++;
            }
            else if (cubes[c[0]][c[1]-1][c[2]] == 0)
            {
                list.push_back({c[0], c[1]-1, c[2]});
                cubes[c[0]][c[1]-1][c[2]] = 2;
            }
        }
        if (c[1] < y_max-1)
        {
            if (cubes[c[0]][c[1]+1][c[2]] == 1)
            {
                nbr_sides++;
            }
            else if (cubes[c[0]][c[1]+1][c[2]] == 0)
            {
                list.push_back({c[0], c[1]+1, c[2]});
                cubes[c[0]][c[1]+1][c[2]] = 2;
            }
        }

        if (c[2] > 0)
        {
            if (cubes[c[0]][c[1]][c[2]-1] == 1)
            {
                nbr_sides++;
            }
            else if (cubes[c[0]][c[1]][c[2]-1] == 0)
            {
                list.push_back({c[0], c[1], c[2]-1});
                cubes[c[0]][c[1]][c[2]-1] = 2;
            }
        }
        if (c[2] < z_max-1)
        {
            if (cubes[c[0]][c[1]][c[2]+1] == 1)
            {
                nbr_sides++;
            }
            else if (cubes[c[0]][c[1]][c[2]+1] == 0)
            {
                list.push_back({c[0], c[1], c[2]+1});
                cubes[c[0]][c[1]][c[2]+1] = 2;
            }
        }

        list.erase(list.begin());
    }

    printf("Done grid - x\n");
    for (int i=0; i<x_max;i++)
    {
        printf("%d,%d,%d,%d\n",cubes[i][0][0],cubes[i][y_max-1][0],cubes[i][0][z_max-1],cubes[i][y_max-1][z_max-1]);
    }
    printf("Done grid - y\n");
    for (int i=0; i<y_max;i++)
    {
        printf("%d,%d,%d,%d\n",cubes[0][i][0],cubes[x_max-1][i][0],cubes[0][i][z_max-1],cubes[x_max-1][i][z_max-1]);
    }
    printf("Done grid - z\n");
    for (int i=0; i<z_max;i++)
    {
        printf("%d,%d,%d,%d\n",cubes[0][0][i],cubes[x_max-1][0][i],cubes[0][y_max-1][i],cubes[x_max-1][y_max-1][i]);
    }
    printf("The surface has %d sides", nbr_sides);
    
    return 0;
}