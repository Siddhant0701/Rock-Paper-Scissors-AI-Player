# Classes

- Ensembler (This is best if implemented using a Keras model system.)

  - Data
    - List of all instantiated models 
    - Histories of games (To a limit of $x$)
    - history_limit
    - *risk_level*

  - Methods
    - Predict: Predicts the next move of the player
    - Accuracy: Calculates the total accuracy achieved by the model in the $x$ most recent games
    - Update: Updates all scores with the new move history

- Prediction-Model

    - Data
      - Histories 
      - Limit
      - Score

    - Inherited Classes
      - Model 0: Random
      - Model 1: Lose to Last Move
      - Model 2: Repeated Moves 
      - Model 3: Patterns
      - Model 4: Weighted Average
