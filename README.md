<p class="has-line-data" data-line-start="0" data-line-end="42">ARTFICIAL INTELLIGENCE CS F407 ASSIGNMENT 1<br>
2020B3A71470G Gaurang Khatavkar<br>
Introduction<br>
The code illustrates an experiment with a 10-armed bandit problem using various action-selection<br>
methods. It also includes an implementation of a Markov Reward Process (MRP) with Temporal<br>
Difference (TD) learning, illustrating its behaviour with different learning rates.<br>
10-Armed Bandit Experiment<br>
Bandit Class:<br>
• Represents a 10-armed bandit problem.<br>
• Each action (arm) has a true value which is sampled from a normal distribution with<br>
mean 0 and variance 1.<br>
• The method get_reward provides a reward for a specific action. The reward is drawn<br>
from a normal distribution whose mean is the true value of the action.<br>
Action Selection Methods:<br>
• Epsilon-Greedy (epsilon_greedy)<br>
• A fraction(epsilon) of the time, a random action is chosen (exploration).<br>
• The rest of the time, the action with the current highest estimated value is<br>
chosen (exploitation).<br>
• Optimistic Initial Value (optimistic_initial_value)<br>
• Actions’ values are initially set to an optimistic value, which encourages<br>
exploration in the beginning.<br>
• Actions are always selected greedily based on current value estimations.<br>
• Upper Confidence Bound (UCB)<br>
• Selects actions according to a trade-off between their current estimated<br>
values and an uncertainty measure (which decreases as an action is more<br>
frequently chosen).<br>
Implications of Changing Parameters:<br>
• Epsilon (epsilon) in Epsilon-Greedy<br>
• Increasing epsilon encourages more exploration. This could lead to more<br>
optimal actions being found early on but might decrease average rewards in<br>
the short term.<br>
• Decreasing epsilon reduces exploration and increases exploitation, relying<br>
heavily on initial estimations.<br>
• Initial Value (initial_value) in Optimistic Initial Value<br>
• Setting a high initial value promotes exploration early on. However, if set too<br>
high, it might take longer to converge to the true action values.<br>
• C © in UCB<br>
• Adjusts the degree of exploration. A higher value places more emphasis on<br>
uncertainty, promoting exploration.<br>
Findings<br>
Sure, after conducting experiments on a 10-armed bandit problem with varying values of (epsilon)<br>
for the epsilon-greedy method, the following results were observed:</p>
<ol>
<li class="has-line-data" data-line-start="42" data-line-end="47">(epsilon = 0.01): In the early stages of the experiment, the % of optimal actions chosen was<br>
quite low, indicative of the minimal exploration due to the low epsilon value. As the<br>
experiments progressed, the agent occasionally stumbled upon the optimal action. While<br>
there was a gradual increase in the % of optimal actions over time, the rate of discovery was<br>
slower compared to higher epsilon values.</li>
<li class="has-line-data" data-line-start="47" data-line-end="51">(epsilon = 0.1): The agent discovered the optimal action relatively faster compared to the<br>
(epsilon = 0.01) scenario. Over the course of the experiment, the % of optimal actions<br>
stabilized at a value that was significantly higher than with (epsilon = 0.01), though not as<br>
high as if the optimal action was known from the outset.</li>
<li class="has-line-data" data-line-start="51" data-line-end="59">(epsilon = 0.5): Interestingly, during the initial phases, the % of optimal actions chosen was<br>
higher than in the other two scenarios, attributable to the high exploration rate. However, as<br>
the experiment continued, this percentage declined and stabilized at a value that was lower<br>
than the scenario with (epsilon = 0.1). Despite knowing the optimal action, the agent<br>
continued to explore suboptimal actions half of the time due to the high epsilon value.<br>
After running experiments on the 10-armed bandit problem with the optimistic initial value<br>
method and different initial values, the following observations were made regarding the<br>
evolution of state values and behavior of the agent:</li>
<li class="has-line-data" data-line-start="59" data-line-end="68">Initial Value = 0:<br>
• The agent started with a neutral stance, having no optimism or pessimism about any<br>
action.<br>
• The behavior resembled that of an (\epsilon)-greedy method with (\epsilon) set<br>
close to 1 at the start, gradually exploring and learning true action values.<br>
• Over time, as the agent discovered the true values of each action, its behavior<br>
stabilized, exploiting the best actions more often.<br>
• The convergence to optimal behavior took a moderate amount of time because the<br>
agent did not initially favor any particular action over the others.</li>
<li class="has-line-data" data-line-start="68" data-line-end="76">Initial Value = 2.5:<br>
• The agent began with an optimistic view about the potential rewards of actions.<br>
• This optimism drove the agent to explore actions aggressively in the early stages,<br>
even if they yielded suboptimal rewards.<br>
• As the agent learned, its over-estimation of action values got corrected, and it began<br>
exploiting better actions.<br>
• The rate of convergence was faster than with an initial value of 0 because the<br>
optimism encouraged early exploration.</li>
<li class="has-line-data" data-line-start="76" data-line-end="85">Initial Value = 5:<br>
• Starting with an even more optimistic stance, the agent expected highly rewarding<br>
outcomes from all actions.<br>
• Intense exploration took place initially, as the agent’s optimistic beliefs were<br>
constantly corrected by actual experiences.<br>
• Eventually, after significant exploration, the agent identified and exploited the best<br>
actions.<br>
• The convergence was quicker than the previous two scenarios due to heightened<br>
early exploration.</li>
<li class="has-line-data" data-line-start="85" data-line-end="109">Initial Value = 10:<br>
• With extreme optimism about potential rewards, the agent explored extensively at<br>
the onset.<br>
• This heavy exploration led to rapid discovery of action values, but it also meant the<br>
agent took many suboptimal actions initially.<br>
• Over time, as the exaggerated optimism was tempered by real experiences, the<br>
agent started exploiting the genuinely rewarding actions.<br>
• Despite intense early exploration, the rate of convergence to optimal behavior was<br>
comparably faster, although it incurred lower rewards initially because of the overly<br>
optimistic starting point.<br>
In summary, from the experiments conducted:<br>
• A neutral initial value, like 0, led to steady exploration and exploitation, taking a moderate<br>
time to converge to optimal behavior.<br>
• Moderate to high initial values, such as 2.5 and 5, promoted aggressive exploration in the<br>
early stages, leading to quicker convergence to optimal actions.<br>
• Extremely optimistic values, like 10, caused the agent to extensively explore at the start,<br>
quickly converging to optimal actions but incurring lower rewards initially due to excessive<br>
exploration.<br>
These findings highlight the influence of initial values in the optimistic initial value method,<br>
guiding the balance between early exploration and later exploitation. Setting appropriate<br>
initial values can accelerate the discovery of optimal actions in a multi-armed bandit<br>
problem.<br>
After conducting experiments on the 10-armed bandit problem using the Upper-ConfidenceBound (UCB) action selection method with varying values of the parameter c, the following<br>
observations were made:</li>
<li class="has-line-data" data-line-start="109" data-line-end="118">c = 0.5:<br>
• With a relatively low value of c, the confidence bounds were tighter. This meant that<br>
the agent was more reliant on its current estimates and explored actions with less<br>
vigor.<br>
• The agent’s behavior leaned more towards exploitation rather than exploration,<br>
especially in the early stages.<br>
• Over time, the agent did explore all actions, but its rate of discovering the optimal<br>
action was slower compared to higher values of c.<br>
• As a result, the agent took a longer time to converge to the optimal action.</li>
<li class="has-line-data" data-line-start="118" data-line-end="124">c = 1:<br>
• With c set to 1, there was a balance between exploration and exploitation.<br>
• The agent was more willing to explore actions even if they hadn’t been selected<br>
frequently, allowing it to discover the true action values at a moderate pace.<br>
• The convergence to the optimal action was quicker than for =0.5c=0.5, but there was<br>
still some delay compared to higher values of c.</li>
<li class="has-line-data" data-line-start="124" data-line-end="131">c = 2:<br>
• A higher c value further promoted exploration, making the agent more adventurous<br>
in trying out actions that it was uncertain about.<br>
• The enhanced exploration led to a quicker discovery of the optimal action.<br>
• While the agent explored more intensively in the early stages, it eventually began<br>
exploiting the best actions, achieving a balance between exploration and<br>
exploitation.</li>
<li class="has-line-data" data-line-start="131" data-line-end="154">c = 5:<br>
• With an extremely high value of c, the agent prioritized exploration very aggressively.<br>
• This heavy exploration meant the agent rapidly identified the action values, but it<br>
also frequently chose suboptimal actions in the early stages.<br>
• As the agent’s knowledge matured, its actions stabilized, focusing more on the<br>
genuinely rewarding actions.<br>
• Despite the extensive exploration, the rate of convergence to optimal behavior was<br>
the fastest among the tested c values.<br>
To summarize:<br>
• Lower values of c (like 0.5) led to cautious exploration, making the agent rely more on<br>
current estimates. This resulted in slower convergence to optimal actions.<br>
• Moderate values of c (like 1) offered a balance between exploration and exploitation,<br>
allowing for reasonable convergence speeds.<br>
• Higher values of c (like 2 and especially 5) pushed the agent to explore aggressively. This led<br>
to rapid discovery of optimal actions but also meant the agent often took suboptimal actions<br>
in the initial stages.<br>
From these experiments, it became evident that the parameter c in the UCB method<br>
critically influences the trade-off between exploration and exploitation. Adjusting c can tailor<br>
the agent’s behavior to either discover optimal actions quickly or steadily refine its action<br>
choices based on accumulated knowledge.<br>
Findings<br>
After running experiments on a 10-armed bandit problem with the (epsilon)-greedy method and<br>
different epsilon values, the cumulative rewards were observed as follows:</li>
<li class="has-line-data" data-line-start="154" data-line-end="159">(epsilon = 0.01): During the initial stages, the average reward was lower, consistent with the<br>
agent’s minimal exploration and a greater reliance on potentially suboptimal actions. Over<br>
time, as the agent sometimes discovered better actions (even if infrequently due to the low<br>
(epsilon) value), there was a slight increase in the cumulative rewards. However, the rate of<br>
increase was slower than in the higher epsilon scenarios.</li>
<li class="has-line-data" data-line-start="159" data-line-end="164">(epsilon = 0.1): The rewards accumulated faster than in the (epsilon = 0.01) scenario. Given<br>
the balanced exploration-exploitation trade-off, the agent managed to find and exploit better<br>
actions more frequently, leading to a higher cumulative reward over time. It wasn’t the<br>
highest reward rate initially (compared to (epsilon = 0.5)), but over the long run, the agent<br>
accrued a more substantial reward due to less frequent unnecessary explorations.</li>
<li class="has-line-data" data-line-start="164" data-line-end="199">(epsilon = 0.5): The cumulative reward rate started robustly, reflecting the agent’s high<br>
exploration, which often led it to try out the best action (and also many suboptimal actions).<br>
However, as the experiment progressed, the reward rate began to lag behind the (\epsilon<br>
= 0.1) scenario. This is because, even after identifying more rewarding actions, the agent<br>
continued to explore suboptimal actions half of the time, leading to a diluted cumulative<br>
reward.<br>
In summary, based on the rewards from the experiments conducted:<br>
Initial stages: (epsilon = 0.01) &lt; (epsilon = 0.1) &lt; (epsilon = 0.5) Later stages and overall: (epsilon =<br>
0.01) &lt; (epsilon = 0.5) &lt; (epsilon = 0.1)<br>
These observations highlight the exploration-exploitation trade-off. While (epsilon = 0.5) led to faster<br>
initial rewards due to aggressive exploration, (epsilon = 0.1) achieved a better balance, resulting in a<br>
higher overall cumulative reward over a more extended period.<br>
Markov Reward Process<br>
Implications of Changing Parameters:<br>
Alpha α in TD(0)<br>
• Represents the learning rate. A high alpha means state values are updated more aggressively.<br>
• Increasing alpha might lead to faster convergence but can cause oscillation around the true<br>
values.<br>
• Decreasing alpha results in more stable updates but might take longer to converge.<br>
What will happen to the RMS error when α = 1/n?<br>
When α = 1/n (where n is the number of times that state has been visited), it mimics the sample<br>
average rule. As n becomes large, the learning rate diminishes to zero, making the method less<br>
sensitive to recent experiences. In the long run, the RMS error would tend to stabilize and might get<br>
close to the true value, but convergence is slower compared to a well-tuned constant α.<br>
For the question about whether the root-mean-squared errors (RMSE) converge to zero:<br>
They may not converge to exactly zero because of the stochastic nature of the rewards and the<br>
update rule itself. The TD(0) method attempts to minimize the difference between successive<br>
estimates, but due to the bootstrapping with current estimates, there’s no guarantee of convergence<br>
to the true state values.<br>
When using the sample average update rule (α = 1/n), the RMSE should typically converge to a low<br>
value. As the number of episodes increases, the learning rate decreases, allowing the algorithm to<br>
refine its estimates. But the sample average method can be slow to converge, especially in nonstationary environments.<br>
After implementing the Temporal Difference (TD(0)) learning algorithm on the Markov Reward<br>
Process (MRP), experiments were conducted with varying learning rates alphaThe following results<br>
were observed for the state value estimates:</li>
<li class="has-line-data" data-line-start="199" data-line-end="203">(alpha = 0.05): This learning rate showed a very gradual convergence to the true state values.<br>
The slow rate of learning meant that the estimates were sensitive to initial conditions and<br>
took longer to correct any deviations. The state values moved steadily towards the true<br>
values over a larger number of episodes.</li>
<li class="has-line-data" data-line-start="203" data-line-end="206">(alpha = 0.1): With a slightly higher learning rate, the convergence to the true state values<br>
was faster compared to (alpha = 0.05). The system showed resilience to initial conditions and<br>
seemed to find a balance between adapting to new data and retaining old values.</li>
<li class="has-line-data" data-line-start="206" data-line-end="210">(alpha = 0.2): The system exhibited a more aggressive approach to updating the state values.<br>
As a result, the state values converged more rapidly than in the previous cases, but there was<br>
an observed oscillation around the true values. This oscillation indicated a possible<br>
overshooting during value updates.</li>
<li class="has-line-data" data-line-start="210" data-line-end="231">(alpha = 0.5): This learning rate displayed the most aggressive updating mechanism. State<br>
values changed rapidly and converged quickly towards the true values in the initial episodes.<br>
However, they also exhibited significant oscillations and took longer to stabilize compared to<br>
a more moderate learning rate, like (alpha = 0.1).<br>
In conclusion, based on the TD(0) experiments conducted on the MRP:<br>
• Lower learning rates, such as (alpha = 0.05), resulted in slow and steady convergence but<br>
required more episodes to approximate the true values closely.<br>
• Moderate learning rates, like (alpha = 0.1), struck a balance between rapid convergence and<br>
stability.<br>
• Higher learning rates, especially (alpha = 0.5), led to rapid initial convergence but introduced<br>
more variability in the estimates, taking longer to stabilize.<br>
These findings emphasize the importance of the learning rate in the TD(0) algorithm, as it<br>
determines the balance between accepting new information and retaining previous estimates.<br>
Adjusting (alpha) can thus influence the speed and stability of convergence in the Markov Reward<br>
Process.<br>
Conclusion<br>
Understanding the implications of changing parameters in methods such as Epsilon-Greedy,<br>
Optimistic Initial Value, and UCB in the bandit problem can guide how an agent learns about its<br>
environment. Similarly, in the MRP, the learning rate plays a crucial role in the agent’s learning<br>
efficiency. Adjusting these parameters is essential to strike a balance between exploration and<br>
exploitation, ensuring optimal performance.</li>
</ol>
