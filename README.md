# stage_simulation

A simulation world made by Stage for eurobot competition and experiment.

### /maps

A png file and a yaml file in same filename is in a group. The shape of the map/obstacle/wall will be defined in the png file, and the parameter such as origin/resolution is written in yaml file.

`eurobot_scenario`: the simulation world for eurobot_empty/2018/2019/2022.

`mapf_experiment`: the simulation world for the experiment Benny Wang needs.

### /scripts

`ground_truth.py`: change the frame_id from odom to map of the topic named "/base_pose_ground_truth", and publish new topic named "/ground_truth".

### /stage

The world file which stage simulator need to includes.

Define reflect/transparent/obstacle/laser/diff_drive_robot, and put them into the world.

### usage

Select the launch file which correspond to the world you need, ex:

```shell
roslaunch stage_simulation eurobot_2018.launch
```
