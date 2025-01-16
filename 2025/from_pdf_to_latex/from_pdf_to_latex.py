import fitz  # PyMuPDF
import re

def pdf_to_txt(pdf_path, txt_path):
    # Открываем PDF и извлекаем текст
    doc = fitz.open(pdf_path)
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        for page in doc:
            txt_file.write(page.get_text())
    doc.close()

def extract_formulas_from_text(text):
    # Регулярное выражение для поиска формул перед цифрами
    # Захватываем формулу и номер в одной строке
    pattern = r'([^\n]*?)([\$(][^()$]*[\$)]\s*$(\d+)$)'

    # Находим все соответствия
    matches = re.findall(pattern, text)

    # Подготовка и вывод результатов
    results = []
    for full_match, formula, number in matches:
        # Удаление $ и обрамляющих символов
        clean_formula = formula.strip('$')
        results.append(f"{full_match.strip()} {clean_formula} \\, ( {number} )")

    return results

# Пример использования
pdf_path = 'sample1.pdf'  # Укажите путь к вашему PDF-файлу
txt_path = 'output.txt'    # Укажите путь для сохранения текстового файла

# Преобразуем PDF в TXT
pdf_to_txt(pdf_path, txt_path)

# Читаем текст из TXT файла
with open(txt_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Извлекаем формулы из текста
results = extract_formulas_from_text(text)

# Печатаем результаты в формате LaTeX
if results:
    print("Найденные формулы:")
    for result in results:
        print(result)
else:
    print("Формулы не найдены.")
