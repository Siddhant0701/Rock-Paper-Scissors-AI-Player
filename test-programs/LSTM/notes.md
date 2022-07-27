[Helpful article](https://towardsdatascience.com/building-a-rock-paper-scissors-ai-948ec424132f)



## Error
- Running into an error where accuracy and val_accuracy doesn't change at all
- Similar error where the metrics keep converging to a specific point and don't move any further


## Ideas
- Could try to add winrate as an input to the model in order to see if the dependency works now.
- Could also add the actions of a computer in order to make that the no assumtions about independant actions are taken.
- Adding synthetic data to see if underfitting can be avoided. There is no way to simulate strategy is synthetic data is chosen.
- If nothing works, it could be worth it to look into RL algorithms to see if any better accuracy rates can be achieved.
- Times between the individual throws.
