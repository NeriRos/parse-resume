from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from pdfminer.high_level import extract_text

load_dotenv()


class ResumeParser:
    def __init__(self, resume_path, *args):
        self.llm = ChatOpenAI()
        self.structure = open('example/structure.json', 'r').read().split('\n')
        self.resume_path = resume_path

    def start(self):
        text = self.parse_resume(self.resume_path)
        return self.extract_structure(text)

    def parse_resume(self, path):
        return extract_text(path)

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
    parsed = ResumeParser('example/resume.pdf').start()
    print(parsed)
