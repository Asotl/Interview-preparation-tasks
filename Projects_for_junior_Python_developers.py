# Word count

# Ask the user what's on their mind. Then after the user responds, count the number of words in the sentence and print that as an output.

# Example:

#     Prompt: what's on your mind today?
#     Input: well, it's just a day for me to be an expert in coding
#     Output: oh nice, you just told me what's on your mind in 13 words!

# To take this a step further, open a file that is handed to you, count the number of words in there, then print it out.

import cups
from xhtml2pdf import pisa

def main():
    with open("text.txt") as file:
        few_words = file.read()
        print(few_words)

    def count_space(coline):
        print(coline) 
        count = len(coline.split())   
        print("space =", count - 1)

    # Имя, для промежуточного файла PDF формата
    filename = "Desktop/pedf.pdf"
	
    # Генерируем контент в виде HTML страницы
    xhtml = f'<h1>{count_space(few_words)}</h1>\n'
    
    def print_pdf(htmlx):      
        pdf = pisa.CreatePDF(htmlx, file(filename, "w"))
        if not pdf.err:
            # Закрываем PDF файл - в противном случае мы не сможем прочитать его
            pdf.dest.close()
        
            # Печатаем файл используя CUPS
            conn = cups.Connection()
            # Получаем список всех принтеров, подключенных к компьютеру
            printers = conn.getPrinters()
            for printer in printers: 
                    # Выводим имя принтера в консоль
                    print(printer, printers[printer]["device-uri"])
                    # Получаем первый принтер со списка принтеров
                    printer_name = printers.keys()[0]
                    conn.printFile(printer_name, filename, "Python_Status_print", {})
        else:
            print("Unable to create pdf file")

    print_pdf(xhtml)


if __name__=="__main__":
    main()

 
