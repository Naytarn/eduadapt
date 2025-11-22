import requests
import json

from config import DEEPSEEK_API_KEY, DEEPSEEK_API_URL


def deepseekApi(user_prompt: str, system_prompt="You are helpful assistant") -> requests:
    """
    function to get a response from deepseek

    Args:
        user_prompt (str): user prompt content
        system_prompt (str): settings for deepseek

    Returns:
        requests: response from AI
    """
    global DEEPSEEK_API_KEY
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {DEEPSEEK_API_KEY}"}
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}],
        "temperature": 0.7,
        "max_tokens": 2048,
    }
    response = requests.post(DEEPSEEK_API_URL, json=data, headers=headers)

    if response.status_code == 200:
        result = response.json()
        return {"status": 200, "data": result["choices"][0]["message"]["content"]}
    else:
        return {"status": response.status_code, "reason": response.text}
    

def get_summarising_test(source_text: str):
    prompt = f"""
ЗАДАЧА:
Составь на основе приведенного ниже текста тест из нескольких вопросов, чтобы проверить, как читатель понял его содержание. Для каждого вопроса сделай несколько вариантов ответа, из которых верным будет только один. Количество вопросов и вариантов ответов определи сам, исходя из длины текста и количества важной информации в нем. При генерации ответа не используй разметку, отправь чистый текст, как указано в шаблоне ниже.

ИСХОДНЫЙ ТЕКСТ: 
{source_text}

ФОРМАТ ОТВЕТА (JSON):
{{
"success": true,
"data": {{
    "questions": [
      {{
        "id": <порядковый номер вопроса, начиная с 1>,
        "question": "<вопрос>",
        "type": "one_choice",
        "options": [
          "<вариант 1>",
          "<вариант 2>", 
          …
        ],
        "correct_answer": <номер правильного ответа>,
        "explanation": "<цитата из текста, по которой можно определить, что данный ответ является правильным>"
      }}
    ],
    "test_config": {{
      "total_questions": <количество вопросов>
    }}
  }},
  "error": null
}}
"""
    return json.loads(deepseekApi(prompt)["data"])