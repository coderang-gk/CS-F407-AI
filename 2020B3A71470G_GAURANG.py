import numpy as np
import matplotlib.pyplot as plt

# Define the 10-armed bandit
class Bandit:
    def __init__(self, k=10):
        self.k = k
        self.action_values = np.random.normal(0, 1, k)
        self.optimal_action = np.argmax(self.action_values)

    def get_reward(self, action):
        return np.random.normal(self.action_values[action], 1)

def epsilon_greedy(Q, epsilon):
    if np.random.random() < epsilon:
        return np.random.randint(len(Q))
    else:
        return np.argmax(Q)

def UCB(Q, N, t, c):
    return Q + c * np.sqrt(np.log(t) / (N + 1e-5))

def run_experiment(bandit, method, **kwargs):
    Q = np.zeros(bandit.k)
    N = np.zeros(bandit.k)
    rewards = []
    optimal_actions = []

    for step in range(1, kwargs.get("num_steps", 1000) + 1):
        if method == "epsilon_greedy":
            action = epsilon_greedy(Q, kwargs.get("epsilon", 0.1))
        elif method == "optimistic_initial_value":
            if step == 1:
                Q = np.full(bandit.k, kwargs.get("initial_value", 5.0))
            action = np.argmax(Q)
        elif method == "ucb":
            action = np.argmax(UCB(Q, N, step, kwargs.get("c", 2)))

        reward = bandit.get_reward(action)
        N[action] += 1
        Q[action] += (reward - Q[action]) / N[action]
        
        rewards.append(reward)
        optimal_actions.append(action == bandit.optimal_action)

    return rewards, optimal_actions

if __name__ == "__main__":
    bandit = Bandit()
    rewards = {}
    optimal_actions = {}

    # Defined parameters to be tested
    epsilons = [0.01, 0.1, 0.5]
    initial_values = [0.0, 2.5, 5.0, 10.0]
    cs = [0.5, 1, 2, 5]  # Varying c values for UCB

    for epsilon in epsilons:
        method = "epsilon_greedy"
        rewards[f"{method}_{epsilon}"], optimal_actions[f"{method}_{epsilon}"] = run_experiment(bandit, method, epsilon=epsilon)

    for initial_value in initial_values:
        method = "optimistic_initial_value"
        rewards[f"{method}_{initial_value}"], optimal_actions[f"{method}_{initial_value}"] = run_experiment(bandit, method, initial_value=initial_value)

    for c in cs:
        method = "ucb"
        rewards[f"{method}_{c}"], optimal_actions[f"{method}_{c}"] = run_experiment(bandit, "ucb", c=c)

    plt.figure(figsize=(10, 5))
    for method, values in rewards.items():
        plt.plot(np.cumsum(values) / np.arange(1, 1001), label=method)
    plt.xlabel("Steps")
    plt.ylabel("Average reward")
    plt.legend()
    plt.title("Average Rewards over Time")
    plt.show()

    plt.figure(figsize=(10, 5))
    for method, values in optimal_actions.items():
        plt.plot(np.cumsum(values) / np.arange(1, 1001), label=method)
    plt.xlabel("Steps")
    plt.ylabel("% Optimal action")
    plt.legend()
    plt.title("% Optimal Actions over Time")
    plt.show()

# Rest of the MRP code remains unchanged...


class MRP:
    def __init__(self):
        # Number of states in our MRP
        self.n_states = 5
        
        # Initialize the state values to zeros for all states
        self.state_values = np.zeros(self.n_states)
    
    def start_episode(self):
        # Always start each episode from state C
        return 2  
    
    def step(self, state):
        """
        Given a state, return the next state and the reward.
        """
        # If the current state is D, the next state is E with a reward of 1
        if state == 3:
            return 4, 1
        # For states A to D, the next state is the immediate next state with a reward of 0
        elif state < 4:
            return state + 1, 0
        # For state E, it remains the same with a reward of 0 (terminal state)
        else:
            return state, 0

    def td_0(self, episodes, alpha):
        """
        Temporal Difference (TD) learning algorithm.
        """
        # Iterate over the number of episodes
        for _ in range(episodes):
            # Start the episode
            state = self.start_episode()
            
            # Loop until the terminal state (E) is reached
            while state != 4:
                next_state, reward = self.step(state)
                
                # Update state value using the TD(0) formula
                self.state_values[state] += alpha * (reward + self.state_values[next_state] - self.state_values[state])
                
                # Move to the next state
                state = next_state

    def rmse(self, true_values):
        """
        Compute Root Mean Squared Error between estimated state values and true state values.
        """
        return np.sqrt(np.mean((self.state_values - true_values) ** 2))


# Given true values from the book
true_values = np.array([1/6, 2/6, 3/6, 4/6, 5/6])

# Define different learning rates for experimentation
alphas = [0.05, 0.1, 0.2, 0.5]
episodes = 100
errors = {}

# Loop over the different learning rates
for alpha in alphas:
    mrp = MRP()  # Create a new MRP instance
    errs = []
    
    # Run the TD(0) algorithm for a number of episodes and track RMSE
    for ep in range(episodes):
        mrp.td_0(1, alpha)
        errs.append(mrp.rmse(true_values))
    
    # Store the RMSE values for this alpha
    errors[alpha] = errs

# Plotting the RMSE values over episodes for each learning rate
for alpha, errs in errors.items():
    plt.plot(errs, label=f'α={alpha}')

plt.xlabel('Episodes')
plt.ylabel('Root Mean Squared Error')
plt.legend()
plt.show()


# Run this program from a terminal and see the output
# Please make sure that the program you submit can be run from a terminal
def main():
    b = Bandit()
    m = MRP()


