#include <iostream>
#include <math.h>

using namespace std;

struct Resources
{
    /* data */
    int ore;
    int clay;
    int obsidian;
    int geode;
};

bool checkResourses(Resources res, Resources cost)
{
    if ((res.ore >= cost.ore) &&
        (res.clay >= cost.clay) &&
        (res.obsidian >= cost.obsidian))
    {
        return true;
    }
    else
    {
        return false;
    }
}

int numberOfStepsToNext(Resources rob, Resources res, Resources cost)
{
    int step = 0;
    int ore_steps = 0;

    if ((cost.obsidian > 0) && (rob.obsidian > 0))
    {
        step = (int)ceil((cost.obsidian-res.obsidian)/rob.obsidian);
        ore_steps = (int)ceil((cost.ore - res.ore)/rob.ore);
        if (ore_steps>step)
        {
            step = ore_steps;
        }
    }
    else if ((cost.clay > 0) && (rob.clay > 0))
    {
        step = (int)ceil((cost.clay-res.clay)/rob.clay);
        ore_steps = (int)ceil((cost.ore - res.ore)/rob.ore);
        if (ore_steps>step)
        {
            step = ore_steps;
        }
    }
    else
    {
        step = (int)ceil((cost.ore-res.ore)/rob.ore);
    }

    return step;
}

Resources payCost(Resources res, Resources cos)
{
    Resources remain;
    
    remain.ore = res.ore - cos.ore;
    remain.clay = res.clay - cos.clay;
    remain.obsidian = res.obsidian - cos.obsidian;
    remain.geode = res.geode - cos.geode;

    return remain;
}

int main()
{
    Resources robot;
    Resources resources;
    Resources ore_robot_cost;
    Resources clay_robot_cost;
    Resources obsidian_robot_cost;
    Resources geode_robot_cost;

    const int minutes = 24;
   
    ore_robot_cost.ore = 2;
    ore_robot_cost.clay = 0;
    ore_robot_cost.obsidian = 0;
    ore_robot_cost.geode = 0;

    clay_robot_cost.ore = 3;
    clay_robot_cost.clay = 0;
    clay_robot_cost.obsidian = 0;
    clay_robot_cost.geode = 0;

    obsidian_robot_cost.ore = 3;
    obsidian_robot_cost.clay = 8;
    obsidian_robot_cost.obsidian = 0;
    obsidian_robot_cost.geode = 0;

    geode_robot_cost.ore = 3;
    geode_robot_cost.clay = 0;
    geode_robot_cost.obsidian = 12;
    geode_robot_cost.geode = 0;

    int max = 0;
        
    // Init
    robot.ore = 1;
    robot.clay = 0;
    robot.obsidian = 0;
    robot.geode = 0;

    resources.ore = 0;
    resources.clay = 0;
    resources.obsidian = 0;
    resources.geode = 0;

    for (int i = 0; (i < minutes); i++)
    {
        int steps_to_next_geode;
        int steps_to_next_obsidian;
        int steps_to_next_clay;
        Resources resorce_if_build;
        Resources robot_if_build;

        Resources robotToBuild;
        robotToBuild.ore = 0;
        robotToBuild.clay = 0;
        robotToBuild.obsidian = 0;
        robotToBuild.geode = 0;
        
        printf("\n   === step %d ===\n", i+1);

        // Start build robot
        if (checkResourses(resources, geode_robot_cost))
        {
            robotToBuild.geode = 1;
            resources = payCost(resources, geode_robot_cost);
            printf("Build geode-collecting robot.\n");
        } 
        
        if (robotToBuild.geode == 0 && 
            checkResourses(resources, obsidian_robot_cost))
        {
            steps_to_next_geode = numberOfStepsToNext(robot, resources, geode_robot_cost);

            resorce_if_build = payCost(resources, obsidian_robot_cost);
            robot_if_build = robot;
            robot_if_build.obsidian += 1;

            if ((steps_to_next_geode == 0) || (steps_to_next_geode >= numberOfStepsToNext(robot_if_build, resorce_if_build, geode_robot_cost)))
            {
                robotToBuild.obsidian = 1;
                resources = payCost(resources, obsidian_robot_cost);
                printf("Build obsidian-collecting robot.\n");
            }

        }

        if ((robotToBuild.obsidian == 0) && 
            (robotToBuild.geode    == 0) && 
            checkResourses(resources, clay_robot_cost))
        {
            steps_to_next_obsidian = numberOfStepsToNext(robot, resources, obsidian_robot_cost);
            resorce_if_build = payCost(resources, clay_robot_cost);
            robot_if_build = robot;
            robot_if_build.clay += 1;

            if (((steps_to_next_geode == 0)    || (steps_to_next_geode    >= numberOfStepsToNext(robot_if_build, resorce_if_build, geode_robot_cost))) &&
                ((steps_to_next_obsidian == 0) || (steps_to_next_obsidian >= numberOfStepsToNext(robot_if_build, resorce_if_build, obsidian_robot_cost))))
            {
                robotToBuild.clay = 1;
                resources = payCost(resources, clay_robot_cost);
                printf("Build clay-collecting robot.\n");
            }
        }

        if ((robotToBuild.clay     == 0) && 
            (robotToBuild.obsidian == 0) && 
            (robotToBuild.geode    == 0) && 
            checkResourses(resources, ore_robot_cost))
        {
            steps_to_next_clay = numberOfStepsToNext(robot, resources, clay_robot_cost);
            resorce_if_build = payCost(resources, ore_robot_cost);
            robot_if_build = robot;
            robot_if_build.ore += 1;

            if (((steps_to_next_geode == 0)    || (steps_to_next_geode    >= numberOfStepsToNext(robot_if_build, resorce_if_build, geode_robot_cost))) &&
                ((steps_to_next_obsidian == 0) || (steps_to_next_obsidian >= numberOfStepsToNext(robot_if_build, resorce_if_build, obsidian_robot_cost))) &&
                ((steps_to_next_clay == 0)     || (steps_to_next_clay     >= numberOfStepsToNext(robot_if_build, resorce_if_build, clay_robot_cost))))
            {
                robotToBuild.ore = 1;
                resources = payCost(resources, ore_robot_cost);
                printf("Build ore-collecting robot.\n");
            }
        }
    
        // Harvest
        resources.ore += robot.ore;
        resources.clay += robot.clay;
        resources.obsidian += robot.obsidian;
        resources.geode += robot.geode;
        if (robot.ore > 0)
        {
            printf("Collect %d ore, Total %d\n", robot.ore, resources.ore);
        }
        if (robot.clay > 0)
        {
            printf("Collect %d clay, Total %d\n", robot.clay, resources.clay);
        }
        if (robot.obsidian > 0)
        {
            printf("Collect %d obsidian, Total %d\n", robot.obsidian, resources.obsidian);
        }
        if (robot.geode > 0)
        {
            printf("Collect %d geode, Total %d\n", robot.geode, resources.geode);
        }

        // Add robot
        robot.ore += robotToBuild.ore;
        robot.clay += robotToBuild.clay;
        robot.obsidian += robotToBuild.obsidian;
        robot.geode += robotToBuild.geode;

        if (robotToBuild.ore > 0)
        {
            printf("One ore robot done, Total %d\n", robot.ore);
        }
        else if (robotToBuild.clay > 0)
        {
            printf("One clay robot done, Total %d\n", robot.clay);
        }
        if (robotToBuild.obsidian > 0)
        {
            printf("One obsidian robot done, Total %d\n", robot.obsidian);
        }
        if (robotToBuild.geode > 0)
        {
            printf("One geode robot done, Total %d\n", robot.geode);
        }

    }

    printf("Number of geodes %d\n", resources.geode);

    return 0;
}