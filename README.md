# irrational-complex-numbers

I recently saw an animation on that demonstrated the concept of irrational numbers, specifically focusing on the Golden Ratio. The animation utilised a variation of Euler's formula, commonly applied in the realms of complex numbers and trigonometry. It featured a double rod pendulum swinging in continuous circles. The animation included periodic zoom-ins to illustrate that the path traced by the pendulum never repeats exactly, forming what appears to be a fractal pattern. Over time, this pattern evolved into an increasingly spherical shape.

The implication was that beauty can never be derived from perfection...I don't know about that, but it seemed like a fun thing to try and recreate and then potentially create another animation using a rational number to compare the differences.

## Setup and Installation

### Python Dependencies

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

### System Dependencies - Linux
If you are running the project on a Linux system, you may need to install `python3-tk` to enable graphical displays with Matplotlib. This can be installed via apt-get:

```
sudo apt-get update
sudo apt-get install python3-tk
```

## Running the project

```
python3 concept.py # or the main.py

```

## Credits and explanation

Found on [@fascinating.fractals](https://www.instagram.com/reel/C0FFe1cI46a/?utm_source=ig_web_copy_link) with this caption:

>The graph is visualized on complex plane, Here is the function :
>
>z(θ)=e^θi + e^Φθi
>
>θ = Angle made by the Inner Arm
>e = Euler's constant
>i = Imaginary number
>
>The first half of the equation e^θi represents the inner arm and second half of the equation represents the outer arm.
>
>This simulation animates the angle θ from 0 to approximately 150000 degrees.
>
>The visual illustrates a setup where the outer arm is rotating golden ratio times faster than the inner arm.
>
>Since the golden ratio is an irrational number with infinite digits, the line would never connect to its starting Position, no matter how long, how fast we run this simulation. If you zoom in you'd always see the gap between those lines. Hence it fills every possible space enclosed within a circle.

### Animations

- **animation1.py** is based on the original concept as described above
- **animiation2.py** is the same as animation1 but the angular velocity of the second arm is increased by the rate of pi after each revolution of the first arm
- **animation3.py** is the same as animation1 but the angular velocity of both arms is increased by the rate of pi after each revolution
- **animiation1a.py** same as animation1 but pretty colour tracings.