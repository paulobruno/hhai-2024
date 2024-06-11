from openai import OpenAI

import prompts
import parseargs


def main():
    client = OpenAI()

    args = parseargs.parse_args()

    prompt = prompts.get_prompt(args.experiment_number)

    print(f"PROMPT:\n\n{prompt}")

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        temperature=0.0,
        seed=42,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )

    print(f"\n\nFULL RESPONSE:\n\n{response}")
    print(f"\n\nRESPONSE TEXT:\n\n{response.choices[0].message.content}")


if __name__ == "__main__":
    main()
