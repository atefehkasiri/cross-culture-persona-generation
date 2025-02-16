import pandas as pd
import functions as fu
import settings as se
 

def llm_auto():
    # Prepare survey questions
    survey_questions = open('file-path.txt','r')
    survey = survey_questions.read()

    # Prepare user data
    user_data = pd.read_csv(f"file-path.csv")
    user_data_list = user_data.values.tolist()

    prompt = [
        {
            "role": "user",
            "content": f"Here is the survey questions:\n{survey}\n\n"
                       f"Here are user data (people's answers to the survey questions):\n{user_data_list} \n\n"
                       f"Generate a minimum number of personas to represent the given user data and answer to all the 31 questions of the survey on behalf of the personas that you created.\n"
                       f"- Rule 1: Do not add any information that does not exist in the user data.\n"
                       f"- Rule 2: You may combine, synthesize, or rephrase multiple user data into a single persona.\n"
                       f"Present only the questions and answers of the generated personas."
        }
    ]

    # get input
    input_prompt = prompt[0]["content"]

    # Display input
    print("\n### Input ###\n")
    print(input_prompt, "\n")

    # save input
    with open("llm_auto/llm_auto_input.txt", "w",) as text_file:
       text_file.write(input_prompt)

    print(f"\n### Waiting for {se.gpt_model}'s response ... ###\n")

    # compute output
    output = fu.chat_completion(prompt)

    # Display output
    print("\n### Output ###\n")
    print(output, "\n")

    # save output
    with open("llm_auto/llm_auto_output.txt", "w") as text_file:
        text_file.write(output)

    print(f"\n### Done. Generated all personas. ###\n")


if __name__ == "__main__":
    # Generating personas
    llm_auto()
