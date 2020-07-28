# 🦊 Abstract Packman Game

- Artificial Intelligence, Search Algorithm Project
- 2020, 18CLC1 HCMUS

![GIF Pacman](/resources/image/pacman_game.png)

> Pacman Agent will find path through the virtual world and collect more foods efficiently. If pacman agent collides with monster, game 'll over.

# 🐱 Requirements 
- [ ] Pacman or monsters moves in 4 directions and cannot move over through the wall
- [ ] Game have four levels
  - [ ] **Level 1**: Pac-man know the food’s position in map and monsters do not appear in
map. There is only one food in the map
  - [ ] **Level 2**: monsters stand in the place ever (never move around). If Pac-man pass
through the monster or vice versa, game is over. There is still one food in the map
and Pac-man know its position
  - [ ] **Level 3**: Pac-man cannot see the foods if they are outside Pacman’s nearest threestep. It means that Pac-man just only scan all the adjacent him (8 tiles x 3). There
are many foods in the map. Monsters just move one step in any valid direction (if
any) around the initial location at the start of the game. Each step Pacman go,
each step Monsters move.
  - [ ] **Level 4 (difficult)**: map is opened. Monsters will seek and kill Pac-man. Pac-man want to get food as much as possible. Pacman will die if at least one monster
passes him. It is ok for monsters go through each other. Each step Pacman go,
each step Monsters move. The food is so many.

>  ## Game points is calculated as following rules
> - Each moving step, your point will be decreased by 1.
> - Each food you take, 20 points will be given for you.
> You may need to run your algorithm on many different graphs to make a comprehensive
comparison of these algorithms’ performance regarding the following aspects:
> - Time to finished
> - The length of the discovered paths
> - Specially, you should generate some difficult maps such as Pac-man is stay among two
monster or wall is around in all side.


# Enviroment
- Language        : `Python`
- Game Engine     : `Pygame`

# Folder Structure
┣ 📂docs\
┣ 📂report\
┣ 📂resources\
┣ 📂src\
┣ ┗ 📂core\
┣ ┗ 📂tests\
┣ ┗ 📂helpers\
┣ 📂tasks
📜DeAI.pdf
📜Readme.md

# Build


# Release Notes

# How to `Hack`

# Credits
👦 👦 👦
* Ho Chi Minh University of Science, *CSC14003* (18CLC1) 2020
- 18127027 Trần Minh Đức
- 18127004 Nguyễn Vũ Thu Hiền
- 18127208 Ngô Thanh Phương Thái
- 18127246 Trần Quốc Tuấn
