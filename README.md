# NIPS2017: Learning to Run

The NIPS 2017 Challenge: [Learning to Run](https://www.crowdai.org/challenges/nips-2017-learning-to-run) is based on the objective to develop a controller to enable a physiologically-based human model to navigate a complex obstacle course as quickly as possible. The human musculoskeletal model and a physics-based simulation environment synthesize physically and physiologically accurate motion. Potential obstacles include external obstacles like steps, or a slippery floor, along with internal obstacles like muscle weakness or motor noise. The score is based on the distance the model travels through the obstacle course in a set amount of time.

## Directories

`/src` contains models and code for training the simulator

## Strategy

The current strategy builds on recent work by Open.ai called [Evolution Strategies as a Scalable Alternative to Reinforcement Learning](https://arxiv.org/abs/1703.03864). The main concept of this approach employs an idea that is similar to genetic algorithms, but updates weights based on perturbations of parameter values according to a normal distribution. This type of algorithm can be effective in environments that require structured exploration, but may not perform as well in environments where good value function estimates are available.


Example:
![HUMAN environment](https://github.com/kidzik/osim-rl/blob/master/demo/training.gif)
