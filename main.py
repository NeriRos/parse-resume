import sys

from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from pdfminer.high_level import extract_text

load_dotenv()


def pdf_to_text(path):
    return extract_text(path)


class ResumeParser:
    def __init__(self, resume_path, structure_path, *args):
        self.llm = ChatOpenAI()
        self.structure = open(structure_path, 'r').read().split('\n')
        self.resume_path = resume_path

    def start(self):
        text = pdf_to_text(self.resume_path)
        return self.extract_structure(text)

    def extract_structure(self, text):
        return self.llm.predict(self.build_prompt(text))

    def build_prompt(self, text):
        return """act as a resume parser.
                           I will give you a desired output structure in json format and a resume. 
                           And you will give me the parsed resume in json format. 
                           The output structure is as follows:
                              """ + '\n'.join(self.structure) + """
                              Resume:
                                """ + text


if __name__ == '__main__':
    resume_path_file = sys.argv[1] if len(sys.argv) > 1 else 'example/resume.pdf'
    structure_path_file = sys.argv[2] if len(sys.argv) > 2 else 'example/structure.json'

    parsed = ResumeParser(resume_path_file, structure_path_file).start()

    print(parsed)
