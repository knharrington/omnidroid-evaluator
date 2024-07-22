# USF COT5402 - Dynamic Programming Project

The goal of this project is to develop an algorithm that evaluates the cost to produce a robot. Designing and implementing the algorithm will require modeling the problem using dynammic programming.

## Input

A text file describing how to assemble the robot and the intermediate products required to construct them. The schematic includes a list of parts and the number of sprockets required to attach the parts.

### Parts

 * **Sprockets** represent the main material component of robots and are used to attach parts to the robot.

 * **Basic parts** are constructed by combining together some number of sprockets in the correct configuration.

 * **Intermediate parts** are constructed via their own assembly process.

 The same part may be used multiple times in the construction of another part. Parts with larger ID values may be used as inputs to parts with smaller ID values.

## Output

The total cost required to make the robot in terms of sprockets used.

## Example

Omnidroid model T9001 is constructed by combining a head assembly, torso assembly, two arm assemblies, and two leg assemblies using 6 sprockets. Head assemblies are constructed by combining an Emote-o-tron computer (14 sprockets) and skull casing (5 sprockets) using 3 sprockets. The torso is a basic part constructed from 24 sprockets. Arms and legs are built from two articulating joint assemblies (4 sprockets each), using 2 sprockets for arms and 6 sprockets for legs. In total, each T9001 omnidroid is built from 100 sprockets.

![omnidroid-example](https://github.com/user-attachments/assets/8166707a-96f6-415c-897c-9fc5947f3406)

