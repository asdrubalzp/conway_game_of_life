
  <h1 align="center">Conway's game of life</h3>


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/asdrubalzp/conway_game_of_life">
    <img src="images/2021-01-06 13-52-52.gif" alt="gameplay" >
  </a>

## About The Project


* It is a zero player game, which means that its evolution is determined by the initial state and does not require any subsequent data entry.
* The "game board" is a flat mesh made up of squares (the "cells") that extend through infinity in all directions. 
Therefore, each cell has 8 "neighboring" cells, which are those that are close to it, including the diagonals. 
* Cells have two states: they are "alive" or "dead" (or "on" and "off").

* The state of cells evolves over discrete units of time.
 The status of all cells is taken into account to calculate their status for the next turn.
 All cells are updated simultaneously on each turn, following these rules:

- A dead cell with exactly 3 living neighboring cells is "born" (that is, the next turn it will be alive).
- A living cell with 2 or 3 living neighboring cells is still alive, otherwise it dies (due to "loneliness" or "overpopulation").

### Built With
* [PyGame](https://www.pygame.org/)
