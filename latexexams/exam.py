import os

class Exam:

    def __init__(
            self,
            target_file,
            vars={},
            template_path="template.tex",
            point_label="Points",
            exercise_label="Exercise"
        ):
        self.target_file = target_file
        self.vars = vars
        self.str_template = open(template_path, "r").read()
        self.elements = []
        self.point_label = point_label
        self.exercise_label = exercise_label
    
    def add_exercise(self, points, code=None, src_file=None, vars={}):
        if src_file is not None:
            code = open(src_file, "r").read()
        elif code is None:
            raise ValueError(f"Cannot add exercise without given code or src_file argument")
        
        # inject content
        for key, content in vars.items():
            code = code.replace("{_" + str(key) + "_}", content)

        
        self.elements.append({
            "type": "exercise",
            "points": points,
            "code": code
        })
    
    def add_page_break(self):
        self.elements.append({
            "type": "pagebreak"
        })

    def compile(self):
        str_exam = self.str_template + ""
        
        # repalce general vars
        for key, val in self.vars.items():
            str_exam = str_exam.replace("{_" + str(key) + "_}", val)
        
        # add code for body
        body = ""
        total_points = 0
        for element in self.elements:
            if element["type"] == "exercise":
                body += "\n" + r"\begin{exercise}" + f"[{element['points']} {self.point_label}]" + element["code"] + "\n" + r"\end{exercise}"
                total_points += element['points']
            elif element["type"] == "pagebreak":
                body += "\n" + r"\clearpage\newpage"
            else:
                raise ValueError(f"Unknown element type {element['type']}")
        str_exam = str_exam.replace("{_body_}", body)
        
        print(f"Prepared code for exam with {total_points} points. Now compiling PDF ...")
        filename = self.target_file
        open(f"src/{filename}.tex", "w").write(str_exam)
        print(f"Writte exam to {filename}")
        os.system(f"pdflatex -output-directory=generated src/{filename}")
        print(f"Compiled exam src/{filename}")
