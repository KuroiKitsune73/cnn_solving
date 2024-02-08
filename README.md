# CNN_Solving
*Finding 1st step of gradient descent in CNN with graphic demonstration*

## **Task from KLE TECH**


*You are given the function f(x,y) = x² + xy + y² and are trying to find a local minimum using gradient descent.*

*You randomly start with x = 1,3 и y = 5,4. Perform the first step of gradient descent with learning rate a = 0,01.*

*Show the resulting values for x and y as well as all of your calculations.*

**1. Analytical solving:**

To perform gradient descent on the function f(x, y) = x^2 + xy + y^2,
you need to calculate the gradient of the function and update the values of the variables x and y in accordance with the gradient descent formula:

x_new=x-a*(δf/δx)

y_new=y-a*(δf/δy)

Where a is the learning rate, and δf/δx and δf/δy are the partial derivatives of the function f with respect to x and y, respectively.

*Calculate the partial derivatives of the function f(x, y):*

δf/δx = 2x + y

δf/δy = 2y+x

*Then substitute the initial values (x = 1.3) and (y = 5.4) into these formulas:*

δf/δx = 2 * 1.3 + 5.4 = 7 

δf/δy = 1.3 + 2 * 5.4 = 12.7

*Now we can update the x and y values using the gradient descent formulas:*

x_new = 1.3 - 0.01 * 7 = 1.226

y_new = 5.4 - 0.01 * 12.7 = 5.273

*Thus, after the first step of gradient descent with (a = 0.01), the new values of the variables (x) and (y) are 1.226 and 5.27*

- If you still have difficulty understanding the gradient descent, imagine a gorge with a large number of stones into which the ball rolls. It rolls to the very bottom on a random trajectory, hitting random depressions and ledges. The process of learning a neural network can be perceived as the release of this ball: **the longer it falls, the closer it is to the minimum of function**.

- The ball that rolls down represents the parameters of the neural network model, and its path down the gorge corresponds to the change in the model parameters with the help of gradient descent.

- In the process of descent, the ball encounters various obstacles in its path, which may be similar to the local minimums of the error function. The longer the ball rolls, the closer it can come to the deepest point of the gorge, which corresponds to minimizing the error function and achieving optimal values of the parameters of the neural network model.*

- **The most difficult thing is to choose the learning step** so that the gradient descent does not diverge and does not take too much time. Sometimes the values of gradients transmitted to the network weights can become very small or very large, which makes it difficult to update the weights and slows down the convergence of the algorithm. In such situations, various methods of normalization and initialization of scales are used, the selection of activation functions is used.
