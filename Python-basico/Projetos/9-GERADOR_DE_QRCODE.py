import qrcode

# cria um QR code com a URL do TikTok
imagem = qrcode.make('https://www.tiktok.com')

# salva o QR code como um arquivo de imagem
imagem.save('meuqrcode.jpg')