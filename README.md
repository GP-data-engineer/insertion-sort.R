# Insertion Sort – Custom R Implementation

![Publication Date] 2020.Feb
*(Created before AI coding assistants became widely available)*

## Overview
This repository contains my **own, manual implementation** of the insertion sort algorithm in **R**.  
The program sorts a one-row matrix of numbers by repeatedly comparing and swapping elements, while printing the intermediate steps of the process.

## Historical Context
This code was originally written **before AI coding assistants were widely available**.  
At that time, there were no AI tools that could prepare this task for me — I developed it **entirely on my own**.  
It reflects my programming skills at that moment, regardless of their level, and serves as an authentic record of my learning process.

## How It Works
- The input is defined as a **1×n matrix** (`tab01`), with several example datasets provided (two commented out).
- The algorithm:
  1. Determines the number of columns (`a1`).
  2. Uses a `for` loop to control the outer passes.
  3. Inside, a `while` loop compares the current element with the previous one.
  4. If the current element is smaller, the two are swapped.
  5. The state of the array is printed after each swap for debugging.
  6. The process continues until no more swaps are needed.
- Global assignment (`<<-`) is used for variables to make them accessible across loops.

## File Structure
- **`insertion-sort.R`** – The R script containing the algorithm and sample data.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/GP-data-engineer/insertion-sort.R.git
