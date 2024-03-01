import preppy
import re

from rlextra.rml2pdf import rml2pdf


def load_aow():
    data = {
        "title": "The Art of War",
        "author": "Sun Tzu",
        "header": "",
        "chapters": {},
        "copyright": "",
    }
    roman_numerals_regex = '(X\\.|V\\.|IX\\.|IV\\.|V?I{1,3}\\.|X?I{1,3}\\.)'
    copyright_delimiter = '----------------------------------------------------------------------'
    regex = f'{roman_numerals_regex}|{copyright_delimiter}'
    split_text = re.split(regex, open("artwar.1b.txt", "r").read())
    for i, text in enumerate(split_text):
        if text:
            if i == 0:
                start_idx = text.index("<html>")
                data['header'] = text[start_idx:].strip("<html><body><pre>\n")
            elif i == len(split_text) - 1:
                data['copyright'] = text.strip("\n\n").strip("\n</pre></body></html>")
            elif re.match(regex, text) != None:
                splitter = "\n\n"
                chapter = split_text[i+1]
                title_break_index = chapter.index("\n\n")
                # replace single newlines with \1 which targets the first capture group followed by a blank space
                replace_1_newline = re.sub('(.)\n(?!\n)', r'\1 ', chapter[title_break_index+len(splitter):])
                data["chapters"][f"{text} {chapter[:title_break_index]}"] = replace_1_newline
    return data


def main():
    art_of_war = load_aow()
    namespace = {'art_of_war': art_of_war}
    template_file_name = 'toc_example.prep'
    template = preppy.getModule(template_file_name)
    rml = template.getOutput(namespace)
    output_pdf_name = 'toc.pdf'
    rml2pdf.go(rml.encode(), outputFileName=output_pdf_name)
    print(f"Generated {output_pdf_name} from {template_file_name}")


if __name__ == '__main__':
    main()
