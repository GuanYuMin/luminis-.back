def template_mail(email , password):
    template = """
            <html>
            <body>
            <p>Estimado usuario, se ha solicitado la recuperación de su contraseña, por favor ingrese a la siguiente dirección para cambiar su contraseña.</p>
            <p>Usuario: """+email+"""</p>
            <p>Contraseña: """+password+"""</p>
            </body>
            </html>
            """
    return template