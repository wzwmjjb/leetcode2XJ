import json
import os.path

with open("assets/chosen_problems_raw.json", "r", encoding="utf-8") as file:
    problems = json.load(file)

formatted_problems = []

difficulty_map = {
    "Easy": 1,
    "Medium": 3,
    "Hard": 5
}

question_dir = "/Users/wangxinran/CLionProjects/CTest/questions"
answer_dir = "/Users/wangxinran/CLionProjects/CTest/answers"

aux_prefix = "<p><strong>Auxiliary Code</strong></p>\n<pre>\n<code class=\"language-c\">\n"
aux_postfix = "</code>\n</pre>"

for problem in problems:
    if not problem["description"]:
        continue

    # get question_code and answer_code
    question_path = os.path.join(question_dir, problem["title"]+".c")
    answer_path = os.path.join(answer_dir, problem["title"]+".c")
    try:
        with open(question_path, "r", encoding="utf-8") as file:
            question_code = file.read()
        with open(answer_path, "r", encoding="utf-8") as file:
            answer_code = file.read()
    except FileNotFoundError:
        print(f"File {problem['title']} is not exist!")
        question_code = ""
        answer_code = ""
    except Exception as e:
        print(f"Error: {e}")
        question_code = ""
        answer_code = ""


    formatted_problem = {
        "type": "编程",
        "title": problem["title"],
        "content": problem["description"] + aux_prefix + question_code +aux_postfix,
        "difficulty": str(difficulty_map.get(problem["difficulty"], 1)),
        "topic": "树与二叉树",
        "tag": "LeetCode",
        "chapter": "第5章",
        "memory": 300,
        "time": 2,
        "testData": [
            {"input": "null", "output": "null"},
            {"input": "null", "output": "null"},
            {"input": "null", "output": "null"},
            {"input": "null", "output": "null"},
            {"input": "null", "output": "null"}
        ],
        "solution": [
            {"language": "C", "code": answer_code},
        ]
    }

    formatted_problems.append(formatted_problem)

with open("assets/chosen_problems_formatted.json", "w", encoding="utf-8") as output_file:
    json.dump(formatted_problems, output_file, ensure_ascii=False, indent=4)

print("Formatted problems saved to 'assets/chosen_problems_formatted.json'")
