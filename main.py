import webview

windows = webview.create_window('Pyscript + Webview', 'index.html')
webview.start(http_server=True)
