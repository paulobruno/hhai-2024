from sklearn import datasets

from DecisionTree import DecisionTree
from prompt_generation import generate_prompt


# prompt experiment 1 -> direct question
def prompt_experiment_1():
    dt = DecisionTree(datasets.load_iris(), random_state=42, max_depth=3)
    return generate_prompt(dt, instance=0)

# prompt experiment 2 -> demonstration
def prompt_experiment_2():
    dt = DecisionTree(datasets.load_iris(), random_state=42, max_depth=3)
    return generate_prompt(dt, instance=0, demonstration=default_demonstration())

# prompt experiment 3 -> instructions
def prompt_experiment_3():
    dt = DecisionTree(datasets.load_iris(), random_state=42, max_depth=3)
    return generate_prompt(dt, instance=0, demonstration=default_demonstration(), add_instructions=True)

# textual characterization 1 -> incorrect classification
def text_experiment_1():
    dt = DecisionTree(datasets.load_iris(), random_state=42, max_depth=3)

    question_text = "Please explain in similar terms why the decision tree concluded that the given example is versicolor with a confidence of 97.06 %."

    return generate_prompt(
        dt,
        instance=0,
        demonstration=default_demonstration(),
        add_instructions=True,
        question_text=question_text,
    )

# textual characterization 2 -> tree representation
def text_experiment_2():
    dt = DecisionTree(datasets.load_iris(), random_state=42, max_depth=3)

    tree_gpt = """Root Node:
    - Feature: Petal Length
    - Condition: If Petal Length ≤ 2.45 cm
    Decision Node 1 (Left Child):
    - Leaf Node: Setosa
    Decision Node 2 (Right Child):
    - Feature: Petal Width
    - Condition: If Petal Width ≤ 1.55 cm
            Decision Node 3 (Left Child):
            - Feature: Petal Length
            - Condition: If Petal Length ≤ 4.95 cm
            - Leaf Node: Versicolor
            - Right Node: Virginica
            Decision Node 4 (Right Child):
            - Feature: Petal Width
            - Condition: If Petal Length ≤ 1.70 cm
            - Leaf Node: Versicolor
            - Right Node: Virginica
"""

    return generate_prompt(
        dt,
        instance=0,
        demonstration=default_demonstration(),
        add_instructions=True,
        tree_representation=tree_gpt,
    )

# textual characterization 3 -> external explanation
def text_experiment_3():
    dt = DecisionTree(datasets.load_iris(), random_state=42, max_depth=3)

    lopez_trigo_tree = """|--- petal width (cm) <= 0.6
|   |--- class: 0
|--- petal width (cm) >  0.6
|   |--- petal width (cm) <= 1.7
|   |   |--- petal length (cm) <= 4.9
|   |   |   |--- class: 1
|   |   |--- petal length (cm) >  4.9
|   |   |   |--- petal width (cm) <= 1.5
|   |   |   |   |--- class: 2
|   |   |   |--- petal width (cm) >  1.5
|   |   |   |   |--- class: 1
|   |--- petal width (cm) >  1.7
|   |   |--- class 2
"""

    lopez_trigo_example = "Given an instance with features: sepal length (cm) = 5.6, sepal width (cm) = 3.0, petal length (cm) = 4.9, and petal width (cm) = 0.6, a good explanation for why the instance was classified as virginica is: 'Iris is type Setosa because its petal-width is low. However, this iris may be also Virginica because its petal-width is quite close to the split value (0.6). It may be also Versicolor because its petal-width and petal-length are quite close to the split values (0.6 and 4.9, respectively).'"

    return generate_prompt(
        dt,
        instance=0,
        demonstration=lopez_trigo_example,
        add_instructions=True,
        tree_representation=lopez_trigo_tree,
    )

# textual characterization 4 -> demonstration for different task
def text_experiment_4():
    dt_wine = DecisionTree(datasets.load_wine(), random_state=42, max_depth=3)

    return generate_prompt(
        dt_wine,
        instance=0,
        demonstration=default_demonstration(),
        add_instructions=True,
    )


def default_demonstration():
    demonstration = "Given an instance of the iris dataset with features: sepal length (cm) = 3.6, sepal width (cm) = 0.8, petal length (cm) = 4.3, and petal width (cm) = 2.9, and a confidence value of 57.81 %, a good explanation for why the instance was classified as virginica is: 'By evaluating the feature values, it is possible to observe that both petal length and petal width are high. This means that by following the decision tree path, the instance should be classified as virginica, although the tree is not very confident in this result.'"
    return demonstration

def get_prompt(experiment_number):
    if experiment_number == 1:
        return prompt_experiment_1()
    elif experiment_number == 2:
        return prompt_experiment_2()
    elif experiment_number == 3:
        return prompt_experiment_3()
    elif experiment_number == 4:
        return text_experiment_1()
    elif experiment_number == 5:
        return text_experiment_2()
    elif experiment_number == 6:
        return text_experiment_3()
    elif experiment_number == 7:
        return text_experiment_4()
    else:
        raise ValueError("Invalid experiment number")
