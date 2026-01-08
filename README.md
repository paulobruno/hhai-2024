# Exploring Large Language Models Capabilities to Explain Decision Trees
Code for the paper "Exploring Large Language Models Capabilities to Explain Decision Trees".

Presented at [Hybrid Human Artificial Intelligence (HHAI) 2024](https://hhai-conference.org/2024/).

## Experiments
A summary containing prompts and responses for all experiments can be found in the [experiments](Experiments.md) file.

## Reproducing the Experiments
### Requirements
- Python >= 3.8
- Scikit-learn
- OpenAI API

### Available Commands
- **Help**
    - `python src/main.py --help`
    - `python src/main.py -h`
    - Show help message.
- **Run experiments by order number**
    - `python src/main.py --experiment-number <experiment_number>`
    - `python src/main.py -n <experiment_number>`
    - Run the experiment with the given number.
    - Valid `<experiment_number>` options: 1, 2, 3, 4, 5, 6, and 7.
- **Run prompt experiments by number**
    - `python src/main.py --prompt-number <prompt_experiment_number>`
    - `python src/main.py -p <prompt_experiment_number>`
    - Run the prompt experiment with the given number.
    - Valid `<prompt_experiment_number>` options: 1, 2, and 3.
- **Run text experiments by number**
    - `python src/main.py --text-number <text_experiment_number>`
    - `python src/main.py -t <text_experiment_number>`
    - Run the text experiment with the given number.
    - Valid `<text_experiment_number>` options: 1, 2, 3, and 4

## Citation
If you use this code for your research, please consider citing this work:
```
@inproceedings{serafim2024exploring,
  title     = {Exploring Large Language Models Capabilities to Explain Decision Trees},
  author    = {Serafim, Paulo Bruno and
    Crescenzi, Pierluigi and
    Gezici, Gizem and
    Cappuccio, Eleonora and
    Rinzivillo, Salvatore and
    Giannotti, Fosca},
  booktitle = {Frontiers in Artificial Intelligence and Applications - HHAI 2024: Hybrid Human AI Systems for the Social Good},
  year      = {2024},
  volume    = {386},
  pages     = {64--72},
  doi       = {10.3233/FAIA240183}
}
```
