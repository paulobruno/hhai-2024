*Disclaimer: although we set the temperature to 0 and use a fixed seed, determinism is not guaranteed from the OpenAI API. Therefore, the results may vary slightly.*

# Prompt Engineering

## Direct Question

### Prompt
```
Consider a dataset that has the following features: sepal length (cm), sepal width (cm), petal length (cm), and petal width (cm). Each instance can be classified into one of the following classes: setosa, versicolor, and virginica. A decision tree was trained on the dataset and the following tree was obtained:
|--- petal length (cm) <= 2.45
|   |--- class: 0
|--- petal length (cm) >  2.45
|   |--- petal width (cm) <= 1.55
|   |   |--- petal length (cm) <= 4.95
|   |   |   |--- class: 1
|   |   |--- petal length (cm) >  4.95
|   |   |   |--- class: 2
|   |--- petal width (cm) >  1.55
|   |   |--- petal width (cm) <= 1.70
|   |   |   |--- class: 1
|   |   |--- petal width (cm) >  1.70
|   |   |   |--- class: 2

An instance has features: sepal length (cm) = 7.3, sepal width (cm) = 2.9, petal length (cm) = 6.3, and petal width (cm) = 1.8.
Please explain in simple terms why the decision tree concluded that the given example is virginica with a confidence of 97.06 %.
```

### Answer
```
The decision tree concluded that the given example is virginica with a confidence of 97.06% because it followed a series of rules based on the features of the instance.

First, it checked if the petal length was less than or equal to 2.45 cm, which was not the case for the given example. Then, it checked if the petal width was less than or equal to 1.55 cm, which was also not the case. Finally, it checked if the petal width was greater than 1.70 cm, which was true for the given example.

Based on these rules, the decision tree determined that the given example belongs to the class virginica with a high confidence of 97.06%.
```

## Demonstration

### Prompt
```
Consider a dataset that has the following features: sepal length (cm), sepal width (cm), petal length (cm), and petal width (cm). Each instance can be classified into one of the following classes: setosa, versicolor, and virginica. A decision tree was trained on the dataset and the following tree was obtained:
|--- petal length (cm) <= 2.45
|   |--- class: 0
|--- petal length (cm) >  2.45
|   |--- petal width (cm) <= 1.55
|   |   |--- petal length (cm) <= 4.95
|   |   |   |--- class: 1
|   |   |--- petal length (cm) >  4.95
|   |   |   |--- class: 2
|   |--- petal width (cm) >  1.55
|   |   |--- petal width (cm) <= 1.70
|   |   |   |--- class: 1
|   |   |--- petal width (cm) >  1.70
|   |   |   |--- class: 2
Given an instance of the iris dataset with features: sepal length (cm) = 3.6, sepal width (cm) = 0.8, petal length (cm) = 4.3, and petal width (cm) = 2.9, and a confidence value of 57.81 %, a good explanation for why the instance was classified as virginica is: 'By evaluating the feature values, it is possible to observe that both petal length and petal width are high. This means that by following the decision tree path, the instance should be classified as virginica, although the tree is not very confident in this result.'
An instance has features: sepal length (cm) = 7.3, sepal width (cm) = 2.9, petal length (cm) = 6.3, and petal width (cm) = 1.8.
Please explain in similar terms why the decision tree concluded that the given example is virginica with a confidence of 97.06 %.
```

### Answer
```
The decision tree classified the given example as virginica with a confidence of 97.06% because it evaluated the feature values and found that both petal length and petal width are high. According to the decision tree path, when petal length is greater than 2.45 and petal width is greater than 1.55, the instance is classified as virginica. In this case, the high values of petal length (6.3 cm) and petal width (1.8 cm) led the decision tree to confidently classify the instance as virginica.
```

## Instructions

### Prompt
```
Consider a dataset that has the following features: sepal length (cm), sepal width (cm), petal length (cm), and petal width (cm). Each instance can be classified into one of the following classes: setosa, versicolor, and virginica. A decision tree was trained on the dataset and the following tree was obtained:
|--- petal length (cm) <= 2.45
|   |--- class: 0
|--- petal length (cm) >  2.45
|   |--- petal width (cm) <= 1.55
|   |   |--- petal length (cm) <= 4.95
|   |   |   |--- class: 1
|   |   |--- petal length (cm) >  4.95
|   |   |   |--- class: 2
|   |--- petal width (cm) >  1.55
|   |   |--- petal width (cm) <= 1.70
|   |   |   |--- class: 1
|   |   |--- petal width (cm) >  1.70
|   |   |   |--- class: 2
Given an instance of the iris dataset with features: sepal length (cm) = 3.6, sepal width (cm) = 0.8, petal length (cm) = 4.3, and petal width (cm) = 2.9, and a confidence value of 57.81 %, a good explanation for why the instance was classified as virginica is: 'By evaluating the feature values, it is possible to observe that both petal length and petal width are high. This means that by following the decision tree path, the instance should be classified as virginica, although the tree is not very confident in this result.'
An instance has features: sepal length (cm) = 7.3, sepal width (cm) = 2.9, petal length (cm) = 6.3, and petal width (cm) = 1.8.
To answer the following question, do not refer to the underlying mechanics of the decision tree in any way, and only refer to the features using natural language. All the relevant features must be mentioned in the answer, but features that were not used by the tree should be ignored. Moreover, do not use any technical jargon or numerical values in the response and prefer to use terms like 'high' and 'low'.
Please explain in similar terms why the decision tree concluded that the given example is virginica with a confidence of 97.06 %.
```

### Answer
```
The decision tree concluded that the given example is virginica with a confidence of 97.06% because the petal length is high and the petal width is also high. This combination of high petal length and petal width led the decision tree to classify the instance as virginica with high confidence.
```

# Textual Representation

## Incorrect Prediction
```
Consider a dataset that has the following features: sepal length (cm), sepal width (cm), petal length (cm), and petal width (cm). Each instance can be classified into one of the following classes: setosa, versicolor, and virginica. A decision tree was trained on the dataset and the following tree was obtained:
|--- petal length (cm) <= 2.45
|   |--- class: 0
|--- petal length (cm) >  2.45
|   |--- petal width (cm) <= 1.55
|   |   |--- petal length (cm) <= 4.95
|   |   |   |--- class: 1
|   |   |--- petal length (cm) >  4.95
|   |   |   |--- class: 2
|   |--- petal width (cm) >  1.55
|   |   |--- petal width (cm) <= 1.70
|   |   |   |--- class: 1
|   |   |--- petal width (cm) >  1.70
|   |   |   |--- class: 2
Given an instance of the iris dataset with features: sepal length (cm) = 3.6, sepal width (cm) = 0.8, petal length (cm) = 4.3, and petal width (cm) = 2.9, and a confidence value of 57.81 %, a good explanation for why the instance was classified as virginica is: 'By evaluating the feature values, it is possible to observe that both petal length and petal width are high. This means that by following the decision tree path, the instance should be classified as virginica, although the tree is not very confident in this result.'
An instance has features: sepal length (cm) = 7.3, sepal width (cm) = 2.9, petal length (cm) = 6.3, and petal width (cm) = 1.8.
To answer the following question, do not refer to the underlying mechanics of the decision tree in any way, and only refer to the features using natural language. All the relevant features must be mentioned in the answer, but features that were not used by the tree should be ignored. Moreover, do not use any technical jargon or numerical values in the response and prefer to use terms like 'high' and 'low'.
Please explain in similar terms why the decision tree concluded that the given example is versicolor with a confidence of 97.06 %.
```

### Answer
```
The decision tree concluded that the given example is versicolor with a confidence of 97.06% because the petal length is high and the petal width is low. This combination of feature values led the tree to classify the instance as versicolor with high confidence.
```

## Tree Text

### Prompt
```
Consider a dataset that has the following features: sepal length (cm), sepal width (cm), petal length (cm), and petal width (cm). Each instance can be classified into one of the following classes: setosa, versicolor, and virginica. A decision tree was trained on the dataset and the following tree was obtained:
Root Node:
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
Given an instance of the iris dataset with features: sepal length (cm) = 3.6, sepal width (cm) = 0.8, petal length (cm) = 4.3, and petal width (cm) = 2.9, and a confidence value of 57.81 %, a good explanation for why the instance was classified as virginica is: 'By evaluating the feature values, it is possible to observe that both petal length and petal width are high. This means that by following the decision tree path, the instance should be classified as virginica, although the tree is not very confident in this result.'
An instance has features: sepal length (cm) = 7.3, sepal width (cm) = 2.9, petal length (cm) = 6.3, and petal width (cm) = 1.8.
To answer the following question, do not refer to the underlying mechanics of the decision tree in any way, and only refer to the features using natural language. All the relevant features must be mentioned in the answer, but features that were not used by the tree should be ignored. Moreover, do not use any technical jargon or numerical values in the response and prefer to use terms like 'high' and 'low'.
Please explain in similar terms why the decision tree concluded that the given example is virginica with a confidence of 97.06 %.
```

### Answer
```
The decision tree classified the given example as virginica with a high confidence because the petal length is high and the petal width is also high. This combination of high petal length and petal width led the decision tree to conclude that the instance belongs to the virginica class.
```

## External Demonstration 1 (high-low instructions)

### Prompt
```
Consider a dataset that has the following features: sepal length (cm), sepal width (cm), petal length (cm), and petal width (cm). Each instance can be classified into one of the following classes: setosa, versicolor, and virginica. A decision tree was trained on the dataset and the following tree was obtained:
|--- petal width (cm) <= 0.6
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
Given an instance with features: sepal length (cm) = 5.6, sepal width (cm) = 3.0, petal length (cm) = 4.9, and petal width (cm) = 0.6, a good explanation for why the instance was classified as virginica is: 'Iris is type Setosa because its petal-width is low. However, this iris may be also Virginica because its petal-width is quite close to the split value (0.6). It may be also Versicolor because its petal-width and petal-length are quite close to the split values (0.6 and 4.9, respectively).'
An instance has features: sepal length (cm) = 7.3, sepal width (cm) = 2.9, petal length (cm) = 6.3, and petal width (cm) = 1.8.
To answer the following question, do not refer to the underlying mechanics of the decision tree in any way, and only refer to the features using natural language. All the relevant features must be mentioned in the answer, but features that were not used by the tree should be ignored. Moreover, do not use any technical jargon or numerical values in the response and prefer to use terms like 'high' and 'low'.
Please explain in similar terms why the decision tree concluded that the given example is virginica with a confidence of 97.06 %.
```

### Answer
```
The decision tree concluded that the given example is virginica with a confidence of 97.06% because its petal width is high, which is a key factor in determining the class. Additionally, its petal length is high, which also contributes to the classification as virginica. These features align closely with the criteria used by the decision tree to classify instances as virginica.
```

## External Demonstration 2 (no high-low instructions)

### Prompt
```
Consider a dataset that has the following features: sepal length (cm), sepal width (cm), petal length (cm), and petal width (cm). Each instance can be classified into one of the following classes: setosa, versicolor, and virginica. A decision tree was trained on the dataset and the following tree was obtained:
|--- petal width (cm) <= 0.6
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
Given an instance with features: sepal length (cm) = 5.6, sepal width (cm) = 3.0, petal length (cm) = 4.9, and petal width (cm) = 0.6, a good explanation for why the instance was classified as virginica is: 'Iris is type Setosa because its petal-width is low. However, this iris may be also Virginica because its petal-width is quite close to the split value (0.6). It may be also Versicolor because its petal-width and petal-length are quite close to the split values (0.6 and 4.9, respectively).'
An instance has features: sepal length (cm) = 7.3, sepal width (cm) = 2.9, petal length (cm) = 6.3, and petal width (cm) = 1.8.
To answer the following question, do not refer to the underlying mechanics of the decision tree in any way, and only refer to the features using natural language. All the relevant features must be mentioned in the answer, but features that were not used by the tree should be ignored.
Please explain in similar terms why the decision tree concluded that the given example is virginica with a confidence of 97.06 %.
```

### Answer
```
The decision tree concluded that the given example is virginica with a confidence of 97.06% because its petal width (1.8 cm) is greater than the split value (1.7 cm), and its petal length (6.3 cm) is also greater than the split value (4.9 cm). These features align with the criteria used by the decision tree to classify instances as virginica.
```

## Different Task Demonstration

### Prompt
```
Consider a dataset that has the following features: alcohol, malic_acid, ash, alcalinity_of_ash, magnesium, total_phenols, flavanoids, nonflavanoid_phenols, proanthocyanins, color_intensity, hue, od280/od315_of_diluted_wines, and proline. Each instance can be classified into one of the following classes: class_0, class_1, and class_2. A decision tree was trained on the dataset and the following tree was obtained:
|--- color_intensity <= 3.82
|   |--- ash <= 3.00
|   |   |--- od280/od315_of_diluted_wines <= 3.73
|   |   |   |--- class: 1
|   |   |--- od280/od315_of_diluted_wines >  3.73
|   |   |   |--- class: 0
|   |--- ash >  3.00
|   |   |--- class: 0
|--- color_intensity >  3.82
|   |--- flavanoids <= 1.58
|   |   |--- alcalinity_of_ash <= 17.65
|   |   |   |--- class: 1
|   |   |--- alcalinity_of_ash >  17.65
|   |   |   |--- class: 2
|   |--- flavanoids >  1.58
|   |   |--- proline <= 724.50
|   |   |   |--- class: 1
|   |   |--- proline >  724.50
|   |   |   |--- class: 0
Given an instance of the iris dataset with features: sepal length (cm) = 3.6, sepal width (cm) = 0.8, petal length (cm) = 4.3, and petal width (cm) = 2.9, and a confidence value of 57.81 %, a good explanation for why the instance was classified as virginica is: 'By evaluating the feature values, it is possible to observe that both petal length and petal width are high. This means that by following the decision tree path, the instance should be classified as virginica, although the tree is not very confident in this result.'
An instance has features: alcohol = 13.16, malic_acid = 2.36, ash = 2.67, alcalinity_of_ash = 18.6, magnesium = 101.0, total_phenols = 2.8, flavanoids = 3.24, nonflavanoid_phenols = 0.3, proanthocyanins = 2.81, color_intensity = 5.68, hue = 1.03, od280/od315_of_diluted_wines = 3.17, and proline = 1185.0.
To answer the following question, do not refer to the underlying mechanics of the decision tree in any way, and only refer to the features using natural language. All the relevant features must be mentioned in the answer, but features that were not used by the tree should be ignored. Moreover, do not use any technical jargon or numerical values in the response and prefer to use terms like 'high' and 'low'.
Please explain in similar terms why the decision tree concluded that the given example is class_0 with a confidence of 100.00 %.
```

### Answer
```
The decision tree classified the given example as class_0 with 100.00% confidence because the value of color intensity is low, and the value of ash is high. This led the tree to directly classify the example as class_0 without considering any other features.
```
