import tkinter as tk  # Importa a biblioteca Tkinter para a criação da interface gráfica
from tkinter import filedialog, messagebox  # Importa funcionalidades de diálogo e mensagens da Tkinter
from fpdf import FPDF  # Importa a biblioteca FPDF para a criação de arquivos PDF
from PIL import Image  # Importa a biblioteca Pillow para manipulação de imagens

# Classe principal do aplicativo
class PDFApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text and Image to PDF Converter")
        self.root.geometry("600x300")  # Define o tamanho da janela principal
        
        # Frame para seleção de funcionalidade
        self.label = tk.Label(root, text="Selecione uma funcionalidade", font=("Arial", 16))
        self.label.pack(pady=20)
        
        # Botão para conversão de texto para PDF
        self.convert_text_button = tk.Button(root, text="Converter Texto para PDF", command=self.open_text_to_pdf_converter, width=40)
        self.convert_text_button.pack(pady=10)
        
        # Botão para conversão de imagem para PDF
        self.convert_image_button = tk.Button(root, text="Converter Imagem para PDF", command=self.open_image_to_pdf_converter, width=40)
        self.convert_image_button.pack(pady=10)
        
    # Abre a janela de conversão de texto para PDF
    def open_text_to_pdf_converter(self):
        converter_window = tk.Toplevel(self.root)
        converter_window.geometry("600x300")  # Define o tamanho da janela secundária
        TextToPDFConverter(converter_window)
        
    # Abre a janela de conversão de imagem para PDF
    def open_image_to_pdf_converter(self):
        converter_window = tk.Toplevel(self.root)
        converter_window.geometry("600x300")  # Define o tamanho da janela secundária
        ImageToPDFConverter(converter_window)

# Classe para conversão de texto para PDF
class TextToPDFConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to PDF Converter")
        self.root.geometry("600x300")  # Define o tamanho da janela

        # Label de instrução
        self.label = tk.Label(root, text="Selecione um arquivo de texto para converter em PDF", font=("Arial", 14))
        self.label.pack(pady=20)

        # Botão para selecionar o arquivo de texto
        self.convert_button = tk.Button(root, text="Selecionar Arquivo", command=self.select_file, width=40)
        self.convert_button.pack(pady=10)

    # Abre o diálogo para selecionar o arquivo de texto
    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            self.convert_to_pdf(file_path)

    # Converte o texto selecionado para PDF
    def convert_to_pdf(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.set_font("Arial", size=12)
            
            # Adiciona o texto ao PDF
            pdf.multi_cell(0, 10, text)
            
            output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
            if output_path:
                pdf.output(output_path)
                messagebox.showinfo("Sucesso", "Arquivo PDF criado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

# Classe para conversão de imagem para PDF
class ImageToPDFConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to PDF Converter")
        self.root.geometry("600x300")  # Define o tamanho da janela

        # Label de instrução
        self.label = tk.Label(root, text="Selecione uma imagem para converter em PDF", font=("Arial", 14))
        self.label.pack(pady=20)

        # Botão para selecionar a imagem e converter para PDF
        self.select_button = tk.Button(root, text="Selecionar Imagem e Converter para PDF", command=self.select_and_convert_image, width=40)
        self.select_button.pack(pady=10)

        self.image_path = None

    # Seleciona a imagem e já inicia o processo de conversão
    def select_and_convert_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
        if file_path:
            self.image_path = file_path
            messagebox.showinfo("Sucesso", "Imagem selecionada com sucesso!")
            self.convert_to_pdf()  # Chama diretamente a conversão após a seleção

    # Converte a imagem selecionada para PDF
    def convert_to_pdf(self):
        if self.image_path:
            try:
                image = Image.open(self.image_path)
                
                # Converte para RGB se a imagem não estiver neste modo
                if image.mode in ("RGBA", "P"):
                    image = image.convert("RGB")
                
                pdf_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
                if pdf_path:
                    # Salva a imagem como PDF
                    image.save(pdf_path, "PDF", resolution=100.0)
                    messagebox.showinfo("Sucesso", "PDF criado com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro ao converter a imagem: {str(e)}")
        else:
            messagebox.showerror("Erro", "Nenhuma imagem selecionada.")

# Inicializa a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = PDFApp(root)
    root.mainloop()
