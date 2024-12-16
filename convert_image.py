from PIL import Image

# Carregar a imagem colorida
def load_image(image_path):
    return Image.open(image_path)

# Converter para tons de cinza
def convert_to_grayscale(image):
    return image.convert('L')

# Converter para imagem binarizada
def convert_to_binary(image, threshold=128):
    # A imagem deve estar em escala de cinza antes de ser binarizada
    grayscale_image = convert_to_grayscale(image)
    binary_image = grayscale_image.point(lambda x: 255 if x > threshold else 0, '1')
    return binary_image

# Salvar imagem

def save_image(image, output_path):
    image.save(output_path)

# Caminho da imagem original
image_path = 'sample_image.jpg'

# Carregar imagem
image = load_image(image_path)

# Converter para tons de cinza e salvar
grayscale_image = convert_to_grayscale(image)
save_image(grayscale_image, 'grayscale_image.jpg')

# Converter para imagem binarizada e salvar
binary_image = convert_to_binary(image)
save_image(binary_image, 'binary_image.jpg')

print('Imagens convertidas e salvas com sucesso!')
