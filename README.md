# Local mending of the {1,3,4}-orientation problem

The idea of **local mending** is introduced in this work:
https://arxiv.org/abs/2102.08703

The **{1,3,4}-orientation problem** is defined in this work:
https://arxiv.org/abs/1702.05456

This program is a simple computational proof that shows that **{1,3,4}-orientations are locally mendable**. More precisely, given any partial solution, one can "patch" any hole by orienting edges within the subgraph induced by a 3 × 3 square.

To try it out, simply run:

    ./mending-134-orientations.py

The program will simply check each possible scenario: after deleting the edges within a 3 × 3 square, what are the possible indegrees of the 8 boundary nodes; there are 1296 cases to check. The program will find a feasible orientation for each case, and it will also print out a solution for each case.

The file [mending-134-orientations.txt](mending-134-orientations.txt) shows what the output will look like.
