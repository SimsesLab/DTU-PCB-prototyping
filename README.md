# DTU-pcbCNC

Guide for producing PCB's from KiCad with DTU Ballerup equipment. 

## What will you need?
- KiCad 9.0+
- A **single-sided** ¹ copper PCB FR4 board.
- Have participated in the safety course held by the professor or TA's.

## What to keep in mind
PCB's made in the course [62733](https://kurser.dtu.dk/course/62733) should preferably be made as **one-sided** PCB ¹. Therefore, make sure to do all of your traces on the back side layer (B.Cu) in the KiCad PCB Editor:
![Design note 1](images-for-guides/kicad_design_note1.png "Design note 1")
A quick check to see if you have selected the correct layer is, if the traces drawn becomes blue.

It can also be a good idea to increase the size of traces for easier result consistency ². 
To do so:
1. go into *Board Setup*.

![Design note 2](images-for-guides/kicad_design_note2.png "Design note 2")

2. Choose the *Net Classes* option under *Design Rules*:

![Design note 3](images-for-guides/kicad_design_note3.png "Design note 3")

3. And change *Clearance* and *Track Width* to **0,8 mm**.

---

> 1: Currently we are limited to one-sided PCB's until further testing and workflows are prepared. The students are free to try their hand ad two-sided PCB's, but should then consult with the people responsible for the machines, and it will be at their own risk and time.

> 2: This step is mostly beneficial for PCB-milling and Fiber-etching.

