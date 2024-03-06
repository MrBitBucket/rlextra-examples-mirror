import preppy
import re

from rlextra.rml2pdf import rml2pdf


def load_document(filename):
    data = {
        "header": "",
        "title": "",
        "author": "",
        "translator": "",
        "chapters": [],
        "copyright": "",
    }
    delimiter = '----------------------------------------------------------------------'
    split_text = open(filename, "r").read().split(delimiter)
    key_info, chapters, copyright_info = split_text[0], split_text[1:-1], split_text[-1]
    data['copyright'] = copyright_info.strip("\n\n")
    key_info_split = key_info.split("\n\n")
    for i, info in enumerate(key_info_split):
        if i == 0:
            data['header'] = info
        elif i == 1:
            title, author = info.split("\n")
            data['title'] = title
            data['author'] = author.replace("By ", "")
        elif i == 2:
            data['translator'] = info.strip("\n")
    for chapter in chapters:
        chapter_split = chapter.split("\n\n")
        chapter_title = chapter_split[1]
        chapter_body = chapter_split[2:]
        data['chapters'].append((chapter_title, chapter_body))
    return data


def main():
    document = load_document("artwar.1b.txt")
    namespace = {'document': document}
    template_file_name = 'longdocument.prep'
    template = preppy.getModule(template_file_name, savePyc=False, importModule=False)
    rml = template.getOutput(namespace)
    output_pdf_name = "_".join(document['title'].lower().split(" ")) + '.pdf'
    rml2pdf.go(rml.encode(), outputFileName=output_pdf_name, saveRml="latest.rml")
    print(f"Generated {output_pdf_name} from {template_file_name}")


if __name__ == '__main__':
    main()
