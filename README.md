Linear Search Visualizer (CISC 121 Project)

This project is an interactive visualizer for the Linear Search algorithm built with Python and Gradio. The app shows each comparison step so users can understand how the algorithm works.

Decomposition
To break the problem down, I separated the linear search algorithm into small steps that the program can follow. Then the algorithm starts at the beginning of the list. At each index, it compares the current number with the target. If they match, the search stops and returns the index. If they don’t match, the algorithm moves to the next index. This continues until the target is found or we reach the end of the list. Lastly, the program lists all the steps in sequence to enable the user to view the progress of the search.

Pattern Recognition
Linear search follows the same repeated pattern for every element in the list. The algorithm always checks one index at a time in order, starting from the beginning and moving forward. At each step, it compares the current value to the target. The pattern never changes: check then compare then decide then move to the next index. This repeated structure makes the algorithm predictable and easy to visualize, because the same comparison happens until the search ends.

Abstraction
For the visualizer, I decided to keep the important details and hide the ones that don’t matter for understanding the algorithm. The important parts to show are the list of numbers, the current index being checked, and whether the value matches the target. The visualization is limited to the comparisons in order to enable the user to have a clear visualization of the step-by-step progress of linear search.

Algorithm Design
The program uses a simple flow: the user inputs a list of numbers and a target value into the Gradio interface.When they are pressing the button, the algorithm processes the list one after the other. For each index, it checks if the value equals the target and records the step. If the value matches, it stops and reports the index.  In case the list does not match, it reports that the target was not found. The output is shown as a list of steps so the user can follow the search visually. The interaction is simplified by the GUI since the user does not need to execute any code, he/she need only to input values and press a button.

Flowchart
![Flowchart](flowchart.png)


https://huggingface.co/spaces/Durrdana/cisc121-linear-search-visualizer 
