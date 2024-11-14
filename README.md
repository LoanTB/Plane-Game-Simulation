# Plane Game Simulation (Alpha)

This project is a flight simulation game built using Python and Pygame. The player controls an aircraft, with visualized speed, altitude, and weapons. The simulation models basic aerodynamics, weapon firing, and environmental interaction, creating an engaging experience for users who want to explore arcade-style flight dynamics.

## Features

- **Aircraft Control**: Move the plane in all directions, accelerate, decelerate, and rotate for full maneuverability.
- **Weapons and Flares**: Fire bullets or release flares to create visual effects and interact with the environment.
- **Flight Dynamics**: The game models basic physics for speed, drag, lift, and gravity, offering a simplified yet immersive flight experience.
- **In-game HUD**: Displays the aircraft’s speed in km/h, Mach speed, and altitude in km, providing real-time feedback on flight status.
- **Environmental Interactions**: The aircraft interacts with the ground, causing particle effects on collision.

## Requirements

- **Python 3.x**
- **Pygame**: Install via pip with `pip install pygame`

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/plane-game-simulation.git
   cd plane-game-simulation
   ```

2. Install Pygame if not already installed:
   ```bash
   pip install pygame
   ```

3. Run the game:
   ```bash
   python main.py
   ```

## Game Controls

- **Arrow Keys (or WASD)**: Control the direction of the aircraft.
- **Up Arrow / W**: Accelerate
- **Down Arrow / S**: Decelerate
- **Left Arrow / A**: Turn Left
- **Right Arrow / D**: Turn Right
- **1 / F**: Fire bullets
- **0 / G**: Release flares
- **O**: End the game

## Project Structure

- **`Player` Class**: Manages the player’s aircraft, including position, orientation, speed, and weapon functions.
- **`Map` Class**: Represents the environment, including the ground level, obstacles, and interactive objects (e.g., bullets, flares).
- **`Game` Class**: Manages user input and game events, updating key states for smooth control of the aircraft.

## Simulation Details

- **Physics Modeling**: The aircraft responds to gravity and friction (air resistance). Player movement is affected by orientation and speed, with acceleration and deceleration calculated to simulate realistic flight motion.
- **Collision Detection**: The aircraft’s position relative to the ground influences speed and collision handling. If the aircraft collides with the ground at high speed, it generates visual particle effects and may be destroyed.
- **Weapons and Effects**: Bullets and flares leave visual trails, enhancing the simulation’s realism and providing feedback on weapon usage.

## HUD Display

The game displays useful flight data:
- **Speed**: Shown in km/h and Mach number.
- **Altitude**: Indicates aircraft height from the ground level.
- **Position**: Displays the current x-coordinate distance.

These metrics update in real-time, helping the player monitor and adjust the aircraft’s flight path.

## Customization

You can adjust various settings and parameters to enhance or alter the experience:
- **Screen Resolution**
- **Ground Level and Object Placement**
- **Aircraft Size, Speed, and Orientation**

These values are set directly within the `Player` and `Map` classes, making it easy to modify the environment or flight dynamics.

## Future Improvements

Potential areas for enhancement:
- **Enhanced Physics**: Improve realism by adding lift and drag calculations.
- **Enhanced Environment**: Add obstacles or dynamic environmental effects.
- **Scoring and Goals**: Introduce objectives, targets, or timed challenges to gamify the experience further.

## License

This project is licensed under the Mozilla Public License 2.0 (MPL-2.0).

### Additional Note on Commercial Use
**Commercial use of this software or any derived works is prohibited without prior written permission from the original author.** For commercial licensing inquiries, please contact loan.tremoulet.breton@gmail.com.
