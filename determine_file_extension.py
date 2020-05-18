file=input("Input the Filename: ")
if '.py' in file:
    print("The extension of the file is: 'python'")
elif '.docx' in file:
    print("The extension of the file is: 'Word document'")
elif '.pptx' in file:
    print("The extension of the file is: 'PowerPoint Presentation'")
elif '.exe' in file:
    print("The extension of the file is: 'executable file'")
elif '.txt' in file:
    print("The extension of the file is: 'Text Document'")
else:
    print("I'm afraid I couldn't determine the extension of your file. Sorry for the inconvenience caused")
