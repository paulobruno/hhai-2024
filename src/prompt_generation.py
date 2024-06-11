def dataset_description(dataset):
    features_text = ", ".join(dataset.feature_names[:-1]) + f", and {dataset.feature_names[-1]}"
    targets_text = ", ".join(dataset.target_names[:-1]) + f", and {dataset.target_names[-1]}"

    description = f"Consider a dataset that has the following features: {features_text}. Each instance can be classified into one of the following classes: {targets_text}."

    return description


def tree_description(classifier_text):
    return classifier_text


def instance_description(dataset, X_test, instance):
    instance_text = f""

    for i in range(len(dataset.feature_names) - 1):
        instance_text += f"{dataset.feature_names[i]} = {X_test[instance,i]}, "

    instance_text += f"and {dataset.feature_names[-1]} = {X_test[instance,-1]}"

    description = f"An instance has features: {instance_text}."

    return description


def instructions():
    instructions_text = "\nTo answer the following question, do not refer to the underlying mechanics of the decision tree in any way, and only refer to the features using natural language. All the relevant features must be mentioned in the answer, but features that were not used by the tree should be ignored. Moreover, do not use any technical jargon or numerical values in the response and prefer to use terms like 'high' and 'low'."

    return instructions_text


def question(dataset, classifier, X_test, y_pred, instance, example=None):
    confidence = classifier.predict_proba([X_test[instance]])
    confidence_text = f"{100.0 * max(confidence[0]):.2f} %"

    question_text = f"Please explain in {'similar' if example else 'simple'} terms why the decision tree concluded that the given example is {dataset.target_names[y_pred[instance]]} with a confidence of {confidence_text}."
    return question_text


def generate_prompt(
    classifier,
    instance,
    demonstration=None,
    add_instructions=False,
    tree_representation=None,
    question_text=None,
):
    prompt_text = f"""{dataset_description(classifier.dataset)} A decision tree was trained on the dataset and the following tree was obtained:
{tree_representation or tree_description(classifier.textual_description())}{demonstration or ""}
{instance_description(classifier.dataset, classifier.X_test, instance)}{instructions() if add_instructions else ""}
{question_text or question(classifier.dataset, classifier.clf, classifier.X_test, classifier.y_pred, instance, demonstration)}"""

    return prompt_text
