from langchain.chat_models import ChatOpenAI
from pdfminer.high_level import extract_text

llm = ChatOpenAI(openai_api_key="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")

structure = open('example/structure.json', 'r').read().split('\n')


def parse_resume(path):
    return extract_text(path)


def extract_structure(text):
    return llm.predict("""act as a resume parser.
                       I will give you a desired output structure in json format and a resume. 
                       And you will give me the parsed resume in json format. 
                       The output structure is as follows:
                          """ + '\n'.join(structure) + """
                          Resume:
                            """ + text)


if __name__ == '__main__':
    resume = parse_resume('example/resume.pdf')
    print(extract_structure(resume))
