#Author: Kartikei Mittal
#ID: 2017KUCP1032
#Date: 30-08-2018
#Program to count keywords, operators and puntuations in a C/C++ program

keywords = ["auto", "const", "double", "float", "int",
            "short", "struct", "unsigned", "break","continue",
            "else","for", "long", "signed","switch", 
            "void", "case", "default", "enum", "goto", 
            "register","sizeof","typedef","volatile",
            "char", "do", "extern", "if", "return",
            "static", "union", "while", "asm", "dynamic_cast",
            "namespace", "reinterpret_cast", "try", "bool", "explicit",
            "new", "static_cast", "typeid", "catch", "false",
            "operator", "template", "typename", "class", "friend",
            "private", "this", "using", "const_cast", "inline",
            "public", "throw", "virtual", "delete", "mutable", 
            "protected", "true", "wchar_t", "include"]

operators = ['<<', '>>', '!=', '==', '>=', '::',
             '<=', '||', '&&', '-=', '/=',
             '*=', '%=', '+=', '--', '++',
             '+', '-', '*', '/', '%', 
             '=','>', '<', '!', '&', '|', '~']

puntuations = [',', '.', ';', '}', '{', '[', ']','(', ')', '#']

keywordDict = dict(zip(keywords, [0]*len(keywords)))
operatorDict = dict(zip(operators, [0]*len(operators)))
puntuationsDict = dict(zip(puntuations, [0]*len(puntuations)))

with open("test.cpp", 'r') as fi:
    data = fi.read()
    fi.close()

    #Removes multi line commments
    while "/*" in data:
        data = data.replace(data[data.find("/*")-1:data.find("*/")+2], "")
    
    #Remove strings
    while '"' in data:
        data = data.replace( 
                    data[ 
                            data.find('"') : 
                            data.find('"', data.find('"')+1)+1 
                        ], ''
                )
    
    for line in data.splitlines():
        if line[0:2] != "//":
            for word in line.split(" "):
                for ch in word:
                    if ch in puntuations:
                        puntuationsDict[ch] = puntuationsDict[ch] + 1
                for key in keywords:
                    if word.find(key) != -1:
                        keywordDict[key] = keywordDict[key] + 1
                        break
                for key in operators:
                    if word.find(key) != -1:
                        operatorDict[key] = operatorDict[key] + 1
                        break


print("Keyword: ", "Count:")
for key in keywordDict.keys():
    if keywordDict[key] != 0:
        print(key, ":", keywordDict[key])

print("\nOperator: ", "Count:")
for key in operatorDict.keys():
    if operatorDict[key] != 0:
        print(key, ":", operatorDict[key])

print("\nPuntuations: ", "Count:")
for key in puntuationsDict.keys():
    if puntuationsDict[key] != 0:
        print(key, ":", puntuationsDict[key])

