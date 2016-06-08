# 291submit
Introduction
This is a poem writer model which we implemented.

Train
In the train function, we didn't set it to run through the whole dataset, cause that would cost too much time. If want to change that, just change the number of iterations.
In the first loop, the number of iterations multiplies batch size equals the number of poems that the model is learning from. 

To train, use the following command:
python train.py

Sample
To sample, you need to come up with a chinese word which you want the poem to start with, and add this word in the command.
python sample.py word
