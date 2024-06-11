import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="""This script is used to execute the experiments presented in the paper 'Exploring Large Language Models Capabilities to Explain Decision Trees', presented at HHAI 2024.""")

    parser.add_argument(
        "-n",
        "--experiment-number",
        type=int,
        default="7",
        help="Pre-defined prompt values for all seven experiments. Valid options are 1 to 7.",
    )

    parser.add_argument(
        "-p",
        "--prompt-number",
        type=int,
        default="0",
        help="Individual prompt experiment number. Valid options are 1, 2, and 3.",
    )

    parser.add_argument(
        "-t",
        "--text-number",
        type=int,
        default="0",
        help="Individual textual characterization experiment number. Valid options are 1, 2, 3, and 4.",
    )

    args = parser.parse_args()

    if args.prompt_number in [1, 2, 3]:
        args.experiment_number = args.prompt_number
    elif args.text_number in [1, 2, 3, 4]:
        args.experiment_number = args.text_number + 3

    return args
