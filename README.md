# DTU Ballerup PCB prototyping

Guide for producing PCB's from KiCad with DTU Ballerup equipment. 

## What will you need?
- KiCad 9.0+
- A **single-sided** ¹ copper PCB FR4 board.
- Have participated in the safety course held by the professor or TA's.

## Contents

- [What to keep in mind](#what-to-keep-in-mind)
- [Making PCBs with the Fiber laser](#making-pcbs-with-the-fiber-laser)
- [Making PCBs with the Roland CNC milling machine](#making-pcbs-with-the-roland-cnc-milling-machine)


## What to keep in mind
PCB's made in the course [62733](https://kurser.dtu.dk/course/62733) should preferably be made as **one-sided** PCB[^1]. Therefore, make sure to do all of your traces on the back side layer (B.Cu) in the KiCad PCB Editor:
![Design note 1](images-for-guides/kicad_design_note1.png "Design note 1")
A quick check to see if you have selected the correct layer is, if the traces drawn becomes blue.

It can also be a good idea to increase the size of traces for easier result consistency[^2].
> [!IMPORTANT]
> This step should be done **before** designing your PCB.
>
> It is **not possible to do afterwards.**

To do so:
1. go into *Board Setup*.

![Design note 2](images-for-guides/kicad_design_note2.png "Design note 2")

2. Choose the *Net Classes* option under *Design Rules*:

![Design note 3](images-for-guides/kicad_design_note3.png "Design note 3")

3. And change both *Clearance* and *Track Width* to **0,8 mm**.

---

[^1]: Currently we are limited to one-sided PCB's until further testing and workflows are prepared. The students are free to try their hand ad two-sided PCB's, but should then consult with the people responsible for the machines, and it will be at their own risk and time.

[^2]: This step is only necessary for PCB-milling and Fiber-etching.

## Making PCBs with the Fiber laser
### Exporting from Kicad:
When choosing to make your PCB with the Fiber laser, you need to do the following steps in Kicad:
#### 1. Open the *Plot* window by going into:
`File - Fabrication Outputs - Gerbers (.gbr)`
![Kicad export step 1](images-for-guides/kicad_export_step1.png "Kicad export step 1")

#### 2. Change *Plot format* to **DXF**, and select where you wish to save your exported file:
![Kicad export step 2](images-for-guides/kicad_export_step2.png "Kicad export step 2")
Be sure to choose a folder you can find, since you will need this file for the actual making of the PCB.
![Kicad export step 3](images-for-guides/kicad_export_step3.png "Kicad export step 3")

#### 3. In the *Plot* window, make sure that the following settings are selected:
![Kicad export step 4](images-for-guides/kicad_export_step4.png "Kicad export step 4")
Where the most important settings are as follows:
   - *Include Layers*: **B.Cu**.
   - *Plot on All Layers*: **Edge.Cuts**
   - *Drill marks*: **Small**
   - *Plot graphic items using their contours*: **Unselected**


---

## Making PCBs with the Roland CNC milling machine
Work in progress