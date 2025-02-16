
import pandas as pd
import functions as fu
import settings as se


def llm_solely():
#change (file-path) to your file path
    # Prepare survey questions
    survey_questions = open('file-path.txt','r')
    survey = survey_questions.read()


    prompt = [
        {
            "role": "user",
            "content": f"Here is the survey questions:\n{survey}\n\n"
                       f"fill out the 31 survey_questions once as a person from Iran .\n"
                       f"show the questions and answers for all of 31 questions for the generated people like a user persona"

        }
    ]

    # get input
    input_prompt = prompt[0]["content"]

    # Display input
    print("\n### Input ###\n")
    print(input_prompt, "\n")

    # save input
    with open("llm_solely/llm_solely_input.txt", "w") as text_file:
        text_file.write(input_prompt)

    print(f"\n### Waiting for {se.gpt_model}'s response ... ###\n")

    # compute output
    output = fu.chat_completion(prompt)

    # Display output
    print("\n### Output ###\n")
    print(output, "\n")

    # save output
    with open("llm_solely/llm_solely_output.txt", "w") as text_file:
        text_file.write(output)

    print(f"\n### Done. Generated all personas. ###\n")


if __name__ == "__main__":
    # Generating personas
    llm_solely()
