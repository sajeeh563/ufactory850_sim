# 🦾 uFactory850 ROS 2 Pick-and-Place Simulation

This project is a complete **ROS 2 (Humble)** simulation of a **uFactory850-style robotic arm** performing an automated **pick-and-place sorting task** in a **Gazebo** environment.  
The system demonstrates object segregation by sorting small parts from a looped channel into **designated bins** based on their shape.

---

## 🎯 Objective

The goal of this project is to design and simulate a **pick-and-place robotic arm system** that can automatically:
- Detect incoming objects from a continuous **U-shaped looped channel**.  
- Grasp objects placed on an **uneven tabletop surface**.  
- Sort them into bins based on their **shape** (circle, square, triangle).  
- Operate in a **cyclic** mode — repeating the pick-and-place sequence continuously.

---

## ⚙️ Features Implemented

- ✅ **ROS 2 Humble Integration** – Built entirely on the stable, long-term support version of ROS 2.  
- ✅ **Custom URDF Model** – A `ufactory850.urdf.xacro` file defines the robotic arm’s 6-axis structure.  
- ✅ **Gazebo Environment** – Simulates a physical workspace with a table, looped channel, and sorting bins.  
- ✅ **Perception Node (Simulated)** – Mimics object detection when parts enter the robot’s workspace.  
- ✅ **Cyclic Pick-and-Place Logic** – Core Python node (`pick_and_place.py`) runs a loop that continuously detects, grasps, and sorts objects.  
- ✅ **Modular Launch Files** – Separate launch configurations for spawning the world, the robot, and visualization.

---

## 🖼️ **Project Output and Verification**

The following screenshot demonstrates the successful execution of the core project logic.

**Terminal Output: Verifying the Pick-and-Place Logic**
![Pick_and_place jpg](https://github.com/user-attachments/assets/20991bd7-c55f-4392-b580-0cac754b8619)

---

## 🛠️ Setup & Execution Instructions

```bash
# 1️⃣ Clone the repository
git clone https://github.com/sajeeh563/ufactory850_sim.git

# Navigate into the project directory
cd ufactory850_sim/

# 2️⃣ Build and Source the Workspace
colcon build
source install/setup.bash

# 3️⃣ Launch the Simulation Environment (spawns robot and world)
ros2 launch ufactory850_sim bringup.launch.py

# 4️⃣ Run the Pick-and-Place Node (starts cyclic sorting logic)
ros2 run ufactory850_sim pick_and_place

---

## ⚠️ **Important Note on Visualization in Virtual Machines**

Issue:  
When running this project within a Virtual Machine (like VirtualBox or VMware), you may experience issues where the Gazebo or RViz2 window appears black, freezes, or fails to render the 3D models.

Technical Reason:  
Gazebo and RViz2 are graphically intensive applications that rely heavily on the computer’s Graphics Processing Unit (GPU) for hardware-accelerated OpenGL rendering.  
Virtual Machines typically emulate graphics hardware or provide limited 3D acceleration support through a process known as software rendering.  
This emulated environment is often not powerful enough to handle the complex 3D scenes of a robotics simulation.

🧠 **This is an environmental constraint, not an error in the project code.**
