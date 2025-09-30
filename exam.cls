\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{exam}[2014/08/16 Example LaTeX class]
\PassOptionsToPackage{letterpaper}{typearea}
\LoadClass[11pt,parskip=half-]{scrarticle}

\usepackage{amssymb,amsmath,amsthm,dsfont,booktabs,tikz,natbib}
\usepackage[mathscr]{euscript}

\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[inner=30mm,outer=30mm,top=20mm,bottom=20mm]{geometry}
\usepackage{textcomp}
\usepackage{eurosym}
\usepackage{hyperref}
\usepackage{ifthen}
\usepackage{comment}
\usepackage{algorithm}
\usepackage{algpseudocode}


\usetikzlibrary{matrix,positioning}

\usepackage{graphicx}
\setkomafont{section}{\rmfamily\bfseries}
\pagestyle{empty}

\theoremstyle{definition}
\newenvironment{exercise}[1][]{\refstepcounter{exercisec}\par\medskip
   \noindent \textbf{Exercise~\theexercisec} (#1) \rmfamily}{}
\theoremstyle{remark}
 
%\input{shortcuts}
\newcounter{exercisec}
\newcounter{sheet}
\newboolean{solutions}
\setboolean{solutions}{false}
\setcounter{exercisec}{0}
\DeclareOption{solutions}{\setboolean{solutions}{true}}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{scrartcl}}
\ProcessOptions\relax

\ifthenelse{\boolean{solutions}}{
\usepackage{framed}
\newenvironment{solution}
    {\begin{framed}{\textbf{Sample Solution}}\\}
    {\end{framed}}
    }
    {\excludecomment{solution}}