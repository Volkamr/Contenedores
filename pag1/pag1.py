from dash import Dash, dcc, html, Input, Output, State, ctx
import os
import subprocess

app = Dash(__name__)

app.layout = html.Div([
    html.Div(dcc.Input(id='input-on-submit', type='text')),
    html.Button('Ingresar', id='submit-val', n_clicks=0),
        html.Button('Cerrar Sesion', id='b_parar', n_clicks=0),
    html.Button('Borrar Perfil', id='b_borrar', n_clicks=0),
    html.Div(id='container-button-basic',
             children='Enter a value and press submit')
])

@app.callback(
    Output('container-button-basic', 'children'),
    Input('submit-val', 'n_clicks'),
    Input('b_parar', 'n_clicks'),
    Input('b_borrar', 'n_clicks'),
    State('input-on-submit', 'value')
)
def update_output(n_clicks, n_clicksp, n_clicksb, value):

    puerto = n_clicks + 8080
    id = '--name ' + str(value)

    if("submit-val" == ctx.triggered_id):
        os.system('docker run ' + id +' -d -p ' + str(puerto) + ':8080 ' + 'usuario python3 pag2.py ')
        link = subprocess.check_output("docker inspect --format \'{{.NetworkSettings.IPAddress}}\' " + str(value), shell=True)

        return 'hola "{}" ingresa a {} '.format(
            value,
            link[0:10].decode("utf-8") + ":8081"
        )

    if("b_parar" == ctx.triggered_id):
        os.system('docker stop ' + str(value))
        return value + ' ha cerrado sesion'
    
    if("b_borrar" == ctx.triggered_id):
        os.system('docker stop ' + str(value))
        os.system('docker rm ' + str(value))
        return value + ' ha borrado su perfil'

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080)